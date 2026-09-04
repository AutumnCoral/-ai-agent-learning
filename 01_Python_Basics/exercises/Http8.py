#泡茶模拟器程序
#1.定义三个任务（模拟泡茶步骤）
import asyncio
import time

#------------同步--------------
def boil_water_sync():
    """同步烧水"""
    print("开始烧水...")
    time.sleep(3)  # 模拟烧水耗时 阻塞三分钟
    print("水开了！")

def prepare_tea_sync():
    """同步准备茶具"""
    print("开始准备茶具...")
    time.sleep(2)  # 模拟准备茶具耗时 阻塞两分钟
    print("茶具准备好了！")

def add_tea_sync():
    """同步放茶叶"""
    print("开始放茶叶...")
    time.sleep(1)  # 模拟放茶叶耗时 阻塞一分钟
    print("茶叶放好了！")


async def boil_water_async():
    """异步烧水"""
    print("开始烧水...")
    await asyncio.sleep(3)  # 模拟烧水耗时
    print("水开了！")

async def prepare_tea_async():
    """异步准备茶具"""
    print("开始准备茶具...")
    await asyncio.sleep(2)  # 模拟准备茶具耗时
    print("茶具准备好了！")

async def add_tea_async():
    """异步放茶叶"""
    print("开始放茶叶...")
    await asyncio.sleep(1)  # 模拟放茶叶耗时
    print("茶叶放好了！")


# ------------2.同步调用-：串行执行-------------
def make_tea_sync():
    """同步泡茶:一个接一个做"""
    print("\n" + "=" * 50)
    print("☕ 同步模式：一件事做完再做下一件")
    print("=" * 50)
    start_time = time.time()
    # 串行执行：必须等烧水完成才能做下一件事情
    boil_water_sync()
    prepare_tea_sync()
    add_tea_sync()
    end_time = time.time()
    print(f"同步泡茶完成，总耗时：{end_time - start_time:.2f} 秒") 
    return end_time

# ------------3.异步调用-：并行执行-------------
async def make_tea_async():
    """异步泡茶:同时做多件事"""
    print("\n" + "=" * 50)
    print("☕ 异步模式：同时做多件事")
    print("=" * 50)
    start_time = time.time()
    # 并行执行：同时烧水、准备茶具、放茶叶
    await asyncio.gather(
        boil_water_async(),
        prepare_tea_async(),
        add_tea_async()
    )
    end_time = time.time()
    print(f"异步泡茶完成，总耗时：{end_time - start_time:.2f} 秒") 
    return end_time

#4.进阶：异步但串行
async def make_tea_async_serial():
    """异步泡茶:异步但串行"""
    print("\n" + "=" * 50)
    print("☕ 异步模式：异步但串行")
    print("=" * 50)
    start_time = time.time()
    # 异步但串行执行：必须等烧水完成才能做下一件事情
    await boil_water_async()
    await prepare_tea_async()
    await add_tea_async()
    end_time = time.time()
    print(f"异步但串行泡茶完成，总耗时：{end_time - start_time:.2f} 秒") 
    return end_time

# 5.主函数
def main():
    print("\n" + "🔥" * 20)
    print("      🍵 泡茶模拟器 - 同步 vs 异步对比")
    print("🔥" * 20)
    
    # 第一步：同步执行
    sync_time = make_tea_sync()
    
    # 第二步：异步执行
    async_time = asyncio.run(make_tea_async())
    
    # 第三步：进阶对比（异步但串行）
    async_serial_time = asyncio.run(make_tea_async_serial())
    
    # ===== 结果对比 =====
    print("\n" + "=" * 50)
    print("📊 最终对比结果")
    print("=" * 50)
    print(f"  同步模式：        {sync_time:.1f} 秒")
    print(f"  异步串行模式：    {async_serial_time:.1f} 秒")
    print(f"  异步并发模式：    {async_time:.1f} 秒")
    print(f"\n🚀 异步并发比同步快了：{sync_time - async_time:.1f} 秒")
    print(f"📈 性能提升：{(sync_time / async_time - 1) * 100:.0f}%")
    print("=" * 50)

if __name__ == "__main__":
    main()