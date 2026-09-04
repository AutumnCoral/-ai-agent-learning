#装饰器
#函数作为一个变量传递，作为参数传递
def decorator(name):
   return f"Hello, {name}"

script = decorator("你好")
print(script) #输出结果：你好
#函数作为一个承参数传递

def call_twice(func, arg):   # 函数作为参数
    return func(arg), func(arg)
second = call_twice(decorator, "理你")
print(second) #输出结果：你好

#手写一个简单的装饰器，装饰器就是给原函数穿个衣服
def my_decorator(func):  # ① 接收原函数
    def wrapper(*args, **kwargs): # ② 创建包装函数
        print("在调用函数之前做一些事情")
        result = func(*args, **kwargs) #    调用原函数
        print("在调用函数之后做一些事情")
        return result  # ③ 返回包装函数
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")