# 类和面向对象：用类描述对象的属性和行为。
class Agent:
    # 类属性：所有 Agent 对象默认共享这个分类。
    category = "AI"

    # 初始化对象的公共属性。
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 返回对象的自我介绍文本。
    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    # __str__ 定义 print() 直接输出对象时显示的内容。
    def __str__(self):
        return f"Agent(name={self.name}, age={self.age})"

    # __repr__ 定义开发和调试时显示对象的内容。
    def __repr__(self):
        return f"Agent(name={self.name}, age={self.age})"


# CodingAgent 继承 Agent，同时增加编程语言属性和代码审查行为。
class CodingAgent(Agent):
    def __init__(self, name, age, language):
        # 调用父类初始化方法，复用 name 和 age 的初始化逻辑。
        super().__init__(name, age)
        self.language = language

    def introduce(self):
        return (
            f"Hello, my name is {self.name}, I am {self.age} years old "
            f"and I code in {self.language}."
        )

    def code_review(self, code):
        """返回一条简单的代码审查结果。"""
        return f"代码审查完成：{code}"


# 创建 CodingAgent 对象，并传入父类和子类需要的参数。
agent = CodingAgent("CodeBuddy", 30, "Python")

# 调用子类重写后的 introduce() 方法。
print(agent.introduce())

# category 没有在子类中定义，因此使用父类的类属性。
print(agent.category)

# 调用子类新增的 code_review() 方法。
print(agent.code_review("print('hello')"))