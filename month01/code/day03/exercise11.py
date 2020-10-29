"""
    while练习, 录入成绩
"""
# 变量
i = 0
sum_grade = 0
# 循环录入5个成绩
while i < 5:
    grade = int(input("请输入成绩："))
    sum_grade += grade
    i += 1

# 计算平均成绩并输出
print(sum_grade / i)