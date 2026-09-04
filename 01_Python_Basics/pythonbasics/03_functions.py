
# 函数：把一段可以重复使用的代码封装起来。

# 默认参数：调用时可以省略 greeting 参数。
def greet(name, greeting="Hello"):
    """向某人打招呼。"""
    return f"{greeting}, {name}!"


print(greet("Alice"))

# 位置参数：按照参数定义的顺序传入值。
def add(a, b):
    return a + b


print(add(5, 3))

# 关键字参数：明确写出参数名，因此参数顺序可以调整。
def multiply(a, b):
    return a * b


print(multiply(b=3, a=4))
