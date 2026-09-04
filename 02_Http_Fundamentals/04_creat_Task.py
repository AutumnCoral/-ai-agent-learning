import asyncio
import time

async def cook_dish(name: str, time_needed: float) -> str:
    """模拟做一道菜"""
    print(f"开始做 {name}...")
    await asyncio.sleep(time_needed)  # 做菜需要的时间
    print(f"{name} 做好了！")
    return f"{name} 完成"

async def main():
    start = time.time()
    
    # ===== 场景1：串行（最慢） =====
    print("\n=== 场景1：串行 ===")
    r1 = await cook_dish("红烧肉", 3)
    r2 = await cook_dish("清蒸鱼", 2)
    r3 = await cook_dish("炒青菜", 1)
    print(f"串行总耗时：{time.time()-start:.1f}秒\n")
    # 总耗时：3+2+1 = 6秒
    
    # ===== 场景2：gather（并发） =====
    print("=== 场景2：gather 并发 ===")
    start = time.time()
    results = await asyncio.gather(
        cook_dish("红烧肉", 3),
        cook_dish("清蒸鱼", 2),
        cook_dish("炒青菜", 1),
    )
    print(f"gather 总耗时：{time.time()-start:.1f}秒\n")
    # 总耗时：3秒（最慢的）
    
    # ===== 场景3：create_task（灵活并发） =====
    print("=== 场景3：create_task 灵活控制 ===")
    start = time.time()
    
    # 先启动两个耗时任务
    task1 = asyncio.create_task(cook_dish("佛跳墙", 5))
    task2 = asyncio.create_task(cook_dish("烤鸭", 4))
    
    # 在这些菜在做的同时，先做点别的
    print("先准备餐具...")
    await asyncio.sleep(1)  # 准备餐具
    print("餐具准备好了！")
    
    # 现在需要菜了，等待它们完成
    result1 = await task1
    result2 = await task2
    
    print(f"create_task 总耗时：{time.time()-start:.1f}秒")
    # 总耗时：5秒（最慢的佛跳墙）
    # 但准备餐具的1秒是在等待过程中完成的，没有额外增加时间

asyncio.run(main())