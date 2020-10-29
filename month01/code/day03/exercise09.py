"""
    while循环练习
"""
# 循环
while True:
    gender = input("请输入性别(男/女)：")

    if gender == "男":
        print("您好先生")
    elif gender == "女":
        print("您好女士")
    else:
        print("性别未知")

    if input("是否继续(y/n):") != "y":
        break