"""
    运算符练习, 求四位整数各位数字之和
"""
# 输入四位整数
number = int(input("请输入四位整数："))

# 计算各位数字相加结果
result = number // 1000 + number // 100 % 10
result += number // 10 % 10 + number % 10

# 输出结果
print("结果为：" + str(result))