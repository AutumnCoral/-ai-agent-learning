#实战 用httpx异步调用API接口
import asyncio
import time
import httpx

# ===== 同步方式：串行调用 5 个 API =====
def sync_call_apis():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
    ]
    start = time.time()
    with httpx.Client(timeout=10) as client:
        for url in urls:
            resp = client.get(url)
            print(f"收到响应，状态码：{resp.status_code}")
    print(f"同步总耗时：{time.time() - start:.1f} 秒")


# ===== 异步方式：并发调用 5 个 API =====
async def async_call_apis():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
    ]
    start = time.time()
    async with httpx.AsyncClient(timeout=10) as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)   # ← 关键：并发！
        for resp in responses:
            print(f"收到响应，状态码：{resp.status_code}")
    print(f"异步总耗时：{time.time() - start:.1f} 秒")


# 运行对比
print("=== 同步模式 ===")
sync_call_apis()
# 同步总耗时：5.x 秒

print("\n=== 异步模式 ===")
asyncio.run(async_call_apis())
# 异步总耗时：1.x 秒    ← 快了近 5 倍！