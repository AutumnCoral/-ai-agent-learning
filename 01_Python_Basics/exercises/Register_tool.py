# 全局工具注册表（字典）
tool_registry = {}

def register_tool(name: str):
    """
    装饰器：将函数注册到 tool_registry 字典中。
    使用 name 作为注册键，函数作为值。
    支持直接用法 @register_tool("search_web") 或 @register_tool（但这里要求带名称）。
    """
    def decorator(func):
        tool_registry[name] = func  # 注册  # 保留原函数元信息
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper  # 返回包装后的函数（也可以直接返回原函数）
    return decorator

# 注册一个工具
@register_tool("search_web")
def search_web(query: str) -> list[str]:
    """搜索网络"""
    return [f"结果: {query}"]

# 注册另一个工具（示例）
@register_tool("calculate")
def calculate(a: float, b: float) -> float:
    """计算两数之和"""
    return a + b

# 使用工具注册表
print(tool_registry["search_web"]("Python"))   # ['结果: Python']
print(tool_registry["calculate"](2, 3))        # 5