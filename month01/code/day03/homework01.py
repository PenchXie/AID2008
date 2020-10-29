"""
    获取人数/重量, 判断电梯是否正常运行
"""
# 输入人数与总重量
people_number = int(input("请输入人数："))
weight = int(input("请输入总重量(kg)："))

# 判断电梯运行状态
state = "正常运行" if people_number <= 10 and weight <= 1000 else "超载"

# 输出结果
print(state)