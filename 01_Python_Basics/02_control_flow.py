# 控制流：根据条件和循环控制代码的执行顺序。
score = 85

# 根据分数判断成绩等级。
if score >= 90:
      grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "D"

# f-string 可以把变量的值嵌入字符串中。
print(f"成绩等级：{grade}")

# for 循环依次输出 0 到 4。
for i in range(5):
    print(i)

print("-------------------------------")

# 使用 for...else 判断 2 到 9 中的质数和合数。
for j in range(2, 10):
    print(f"当前数字为：{j}")

    # 尝试使用 2 到 j - 1 之间的数字去除 j。
    for x in range(2, j):
        print(f"当前数字为：{j}，当前除数为：{x}")
        if j % x == 0:
            print(f"{j} 等于 {x} * {j // x}")
            break
    else:  # 没有遇到 break，说明 j 没有因数，是质数。
        print(f"{j} 是质数")