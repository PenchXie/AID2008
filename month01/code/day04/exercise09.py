"""
    容器通用操作, 数学运算符练习, 根据输入数字打印整数
"""
# # 循环
# while True:
#     number_str = input("请输入一个正整数:")
#     if number_str == "":
#         break
#     # 处理特殊情况(1, 2)
#     elif number_str == "1":
#         print("*")
#         continue
#     elif number_str == "2":
#         print("**\n**")
#         continue
#     # 一般情况(>2)
#     number = int(number_str)
#     print("*" * number)
#     for i in range(number - 2):
#         print("*%s*" % (" " * (number - 2)))
# #     print("*" * number)
#
# 更好的写法
while True:
    number_str = input("请输入一个整数：")
    if number_str == "":
        break
    number = int(number_str)
    for i in range(number):
        if i == 0 or i == number -1:
            print("*" * number)
        else:
            print("*%s*" % (" " * i))
