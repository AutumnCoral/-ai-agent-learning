#装饰器实战
import functools

def cache_result(func):
    """
    装饰器：缓存函数计算结果。
    相同参数调用时直接返回缓存值，不再重复计算。
    """
    cache = {}  # 缓存字典，键为参数元组，值为函数返回值

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 构造可哈希的缓存键（参数必须可哈希，否则需额外处理）
        # 将位置参数和关键字参数统一成元组
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

# 示例用法
@cache_result
def slow_add(a, b):
    print(f"正在计算 {a} + {b} ...")
    return a + b

print(slow_add(2, 3))  # 打印计算过程
print(slow_add(2, 3))  # 直接返回缓存，不再打印
print(slow_add(3, 2))  # 参数顺序不同，重新计算（因为 key 不同）