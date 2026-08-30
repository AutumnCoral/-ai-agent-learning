#判断是否为质数
def is_prime(n: int) -> bool:
    """
    判断一个数是否为质数。

    参数:
        n (int): 要判断的数

    返回:
        bool: 如果是质数返回 True，否则返回 False
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True