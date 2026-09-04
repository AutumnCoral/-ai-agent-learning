#Python的数据结构
#集合list
sex = [1,'2',False,3.14]
print(sex)
print(type(sex))
print(sex.insert(0, "new_item"))#指定位置插入，返回None
print(sex)#返回["new_item"1, '2', False, 3.14]
print(sex.pop())#删除最后一个元素
print(sex)
print(sex[0])#访问第一个元素
print(sex[1:3])#访问第二个到第三个元素
print(sex[-1])#访问最后一个元素
print(sex.extend([4,5,6]))#在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） 
print(sex)#输出结果print(sex)
print(sex.count(1))#统计某个元素在列表中出现的次数  
print(sex.index(1))#从列表中找出某个值第一个匹配项的索引位置，索引为1
print(sex.reverse())#反向列表中元素 ,返回None
print(sex)

# 字典（dict）：由键（key）和值（value）组成的键值对集合
# 创建一个保存模型配置的字典
config = {
    "model": "deepseek-v3",
    "temperature": 0.7,
    "max_tokens": 4096
}

# 通过键访问值；如果键不存在，会抛出 KeyError
print(config["model"])

# 使用 get() 安全访问；键不存在时返回默认值 1.0
print(config.get("top_p", 1.0))

# 添加一个新键值对；如果键已存在，则会修改原来的值
config["stream"] = True
print(config)

# keys() 返回字典中所有的键
print(config.keys())

# values() 返回字典中所有的值
print(config.values())

# items() 返回所有键值对，每一项都是 (key, value) 元组
print(config.items())

#推导式（Comprehension）
#列表推导式
#普通列表
squares = []
for x in range(10):
    squares.append(x**2) #在列表尾部添加元素（原地修改，不返回新列表）
print(squares)
#列表推导式
squares = [x**2 for x in range(10)] #返回新列表
print(squares)
# 带条件过滤
evens = [i for i in range(10) if i % 2 == 0]
# 结果：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(evens)

# 调转键值对
# 构建一个工具名→工具描述映射
tool_map = {
    "search": "搜索网络",
    "read": "读取文件",
    "write": "写入文件",
}
reversed_map = {v: k for k, v in tool_map.items()}
# 结果：{'搜索网络': 'search', '读取文件': 'read', '写入文件': 'write'}
unique_lengths = {len(word) for word in ["ai", "agent", "python", "code"]}
# 结果：{2, 4, 5, 6}集合没有顺序
print(unique_lengths)
unique_lengths = [len(word) for word in ["ai", "agent", "python", "code"]]
# 结果：{2, 4, 5, 6}#列表是有序的
print(unique_lengths)
unique_lengths = (len(word) for word in ["ai", "agent", "python", "code"])
# <generator object <genexpr> at 0x...>
print(unique_lengths)
print(list(unique_lengths))#查看生成器里的值 [2, 5, 6, 4]