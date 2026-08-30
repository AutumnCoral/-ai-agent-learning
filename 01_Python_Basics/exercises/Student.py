class Student:
    """
    学生类，包含姓名和各科成绩。

    属性:
        name (str): 学生姓名
        scores (dict[str, float]): 科目名称到分数的映射字典
    """

    def __init__(self, name: str, scores: dict[str, float]):
        """
        初始化学生对象。

        参数:
            name (str): 学生姓名
            scores (dict[str, float]): 科目及对应分数，例如 {"数学": 95, "英语": 88}
        """
        self.name = name
        self.scores = scores

    def average_score(self) -> float:
        """
        计算所有科目的平均分。

        返回:
            float: 平均分（保留两位小数，可根据需求调整）
        """
        if not self.scores:
            return 0.0
        total = sum(self.scores.values())
        return total / len(self.scores)

    def best_subject(self) -> str:
        """
        返回分数最高的科目名称。

        返回:
            str: 最高分对应的科目名；如果成绩为空，返回空字符串。
        """
        if not self.scores:
            return ""
        # 使用 max 函数，key 指定比较依据为分数值
        best = max(self.scores, key=self.scores.get)
        return best