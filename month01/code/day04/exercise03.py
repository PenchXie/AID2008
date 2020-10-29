"""
    for循环练习, 整数位累加
"""
# 输入一个整数
num = input("请输入一个整数：")

total = 0
# 循环
for item in num:
    total += int(item)

# 输出结果
print(total)

# # 另一种写法
# num = int(input("请输入一个整数："))
#
# total = 0
# while num:
#     total += num % 10
#     num = num // 10
#
# print(total)