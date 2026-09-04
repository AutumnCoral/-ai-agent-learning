#实战 4：信号量（Semaphore）限制并发数
import asyncio
import httpx

async def limited_api_call(
    client: httpx.AsyncClient,
    sem: asyncio.Semaphore,
    item_id: int,
) -> dict:
    """受信号量限制的 API 调用"""
    async with sem:   # ← 进入时信号量 -1，满了就等待；退出时信号量 +1
        print(f"[{item_id}] 开始请求...")
        await asyncio.sleep(0.5)  # 模拟 API 调用
        print(f"[{item_id}] 完成")
        return {"id": item_id, "status": "ok"}


async def batch_with_limit(total: int = 20, max_concurrent: int = 5):
    """
    批量请求，但最多同时进行 5 个。
    5 个完成一个，就放行下一个——始终保持不超过 5 个在跑。
    """
    sem = asyncio.Semaphore(max_concurrent)  # 信号量，初始值 5

    async with httpx.AsyncClient() as client:
        tasks = [
            limited_api_call(client, sem, i)
            for i in range(total)
        ]
        results = await asyncio.gather(*tasks)

    print(f"全部 {total} 个请求完成")
    return results

asyncio.run(batch_with_limit(total=20, max_concurrent=5))
# 20 个请求，最多 5 个并发 → 分 4 批完成 → 总耗时 ≈ 4 × 0.5 = 2 秒