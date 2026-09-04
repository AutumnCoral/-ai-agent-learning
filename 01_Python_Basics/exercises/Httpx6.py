#并发搜索——同时查多个数据源，合并结果
import httpx
import asyncio
# 1. 模拟搜索一个数据源
async def search_source(
    client: httpx.AsyncClient,
    name: str,
    query: str,
) -> dict:
    """模拟搜索一个数据源"""
    await asyncio.sleep(1)       # 模拟网络延迟
    return {
        "source": name,
        "results": [f"{name} 中关于 '{query}' 的结果 1", f"结果 2"],
    }
# 2. 同时搜索多个数据源，合并结果
async def concurrent_search(query: str) -> list[dict]:
    """同时搜索多个数据源，合并所有结果"""
    sources = ["文档库", "代码库", "知识图谱", "网络搜索", "历史记录"]

    async with httpx.AsyncClient() as client:
        tasks = [
            search_source(client, source, query)
            for source in sources
        ]
        # gather 等待所有完成。也可以用 as_completed 先展示快的
        all_results = await asyncio.gather(*tasks, return_exceptions=True)

    # 分离成功和失败
    success = []
    for result in all_results:
        if isinstance(result, Exception):
            print(f"[警告] 某个搜索源失败：{result}")
        else:
            success.append(result)

    print(f"成功搜索 {len(success)}/{len(sources)} 个数据源")
    return success

# 5 个源并发查询，总耗时 ≈ 1 秒（不是 5 秒）
# result = asyncio.run(concurrent_search("AI Agent 架构"))