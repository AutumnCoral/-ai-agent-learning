#异步：发起一个操作后不干等，切换到其他任务。"
import asyncio
import time

async def boil_water():
    print("开始烧水...")
    await asyncio.sleep(5)     # ← 不卡！把控制权交出去，让其他任务跑
    print("水烧好了！")

async def wash_cup():
    print("洗茶杯...")
    await asyncio.sleep(1)
    print("茶杯洗好了！")

async def add_tea():
    print("放茶叶...")
    await asyncio.sleep(0.5)
    print("茶叶放好了！")

async def main():
    print("=== 异步模式 ===")
    start = time.time()
    # 同时启动三个任务，总耗时≈最慢的那个
    await asyncio.gather(
        boil_water(),
        wash_cup(),
        add_tea(),
    )
    print(f"总耗时：{time.time() - start:.1f} 秒")
asyncio.run(main())