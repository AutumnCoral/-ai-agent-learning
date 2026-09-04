#同步 一件事做完再做下一件
import time

def boil_water():
    print("开始烧水...")
    time.sleep(5)        # ← 在这里"卡住"5 秒，什么都不干
    print("水烧好了！")

def wash_cup():
    print("洗茶杯...")
    time.sleep(1)
    print("茶杯洗好了！")

def add_tea():
    print("放茶叶...")
    time.sleep(0.5)
    print("茶叶放好了！")

# 同步执行：一个接一个，总耗时 = 5 + 1 + 0.5 = 6.5 秒
print("=== 同步模式 ===")
start = time.time()
boil_water()      # 卡 5 秒
wash_cup()        # 卡 1 秒
add_tea()         # 卡 0.5 秒
print(f"总耗时：{time.time() - start:.1f} 秒")