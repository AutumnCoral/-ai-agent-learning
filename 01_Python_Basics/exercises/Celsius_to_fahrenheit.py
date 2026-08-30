
#温度转换器： 写一个函数 celsius_to_fahrenheit(c: float) -> float 和 fahrenheit_to_celsius(f: float) -> float。加上类型注解和 docstring。
# def celsius_to_fahrenheit(c: float) -> float:
#     """
#     将摄氏度转换为华氏度。

#     参数:
#         c (float): 摄氏温度值

#     返回:
#         float: 对应的华氏温度值
#     """
#     return c * 9 / 5 + 32
def celsius_to_fahrenheit(c: float) -> float:
    """
    将摄氏度转换为华氏度。

    参数:
        c (float): 摄氏温度值

    返回:
        float: 对应的华氏温度值
    """
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f: float) -> float:
    """
    将华氏度转换为摄氏度。

    参数:
        f (float): 华氏温度值

    返回:
        float: 对应的摄氏温度值
    """
    return (f - 32) * 5 / 9