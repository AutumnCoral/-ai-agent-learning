from ast import main
import asyncio

async def boil_water():
    await asyncio.sleep(5)
    return "水烧好了！"

async def wash_cup():
    await asyncio.sleep(1)
    return "茶杯洗好了！"

async def add_tea():
    await asyncio.sleep(0.5)
    return "茶叶放好了！"

# #携程的三种形式，方式一：asasync.gather-并发裕裕运行多个协程
#     # 并发执行三个任务
#     results = await asyncio.gather(
#         boil_water(),
#         wash_cup(),
#         add_tea()
#     )
#     # 打印所有结果
#     for result in results:
#         print(result)

# # 启动程序
# asyncio.run(main())


# ===== 方式 1：asyncio.run() — 程序的"入口点" ,直接运行协程并获取返回值=====
# result = asyncio.run(boil_water())
# print(result)  


# ===== 方式 2：await — 在已有的协程中调用另一个协程 =====
async def main():
    result1 = await add_tea() 
    result2 =await boil_water() 
    result3 = await wash_cup()  # ← 等待 say_hello 完成，拿到返回值
    print(result1 ,result2,result3)                      # Hello, Agent!
asyncio.run(main())

#asyncio.create_task()