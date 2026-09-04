#带超时 + 重试的异步 API 调用
import httpx  # HTTP 客户端库
import asyncio  # 异步支持库

#1. 核心函数：带重试的 API 调用，async def 表示这是异步函数，返回一个协程对象。
async def call_api_with_retry(
    client: httpx.AsyncClient,  # 参数1：异步HTTP客户端
    url: str,                   # 参数2：请求的URL
    max_retries: int = 3,       # 参数3：最大重试次数，默认3次
    timeout: float = 10.0,      # 参数4：超时时间（秒），默认10秒
) -> dict:                      # 返回值：字典
    """
    异步 API 调用：超时保护 + 指数退避重试。

    注意这是异步版本，和 1.2 节的同步重试逻辑对比。
    """
    for attempt in range(max_retries):
        try:
            response = await asyncio.wait_for(
                client.get(url),
                timeout=timeout,
            )
            response.raise_for_status() #检查状态码
            return response.json() # 将 JSON 响应解析为 Python 字典

        except asyncio.TimeoutError:
            if attempt == max_retries - 1:
                raise RuntimeError(f"请求超时（{timeout}s），已重试 {max_retries} 次")
            wait = 2 ** attempt
            print(f"[超时] {wait}s 后重试...")
            await asyncio.sleep(wait)

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:
                retry_after = int(e.response.headers.get("Retry-After", 5))
                print(f"[429 限流] 等待 {retry_after}s")
                await asyncio.sleep(retry_after)
            elif e.response.status_code >= 500:
                wait = 2 ** attempt
                print(f"[{e.response.status_code} 服务器错误] {wait}s 后重试...")
                await asyncio.sleep(wait)
            else:
                raise  # 4xx 不重试

# 使用
async def main():
    async with httpx.AsyncClient() as client:
        result = await call_api_with_retry(client, "https://httpbin.org/json")
        print(result)
#程序入口
asyncio.run(main())