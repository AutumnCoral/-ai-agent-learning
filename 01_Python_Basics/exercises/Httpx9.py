#2. 并行 vs 串行
#写一个函数 fetch_all_urls(urls: list[str])，先用串行方式（for 循环 + await）实现，再用 asyncio.gather() 实现，对比两者的执行时间。URL 可以用 https://httpbin.org/delay/1（复制 3 次）。
 