"""
    while练习５, 生成一个随机数让玩家猜
"""
# 导入随机数的库
import random

# 生成随机数
random_number = random.randint(1, 100)

# # 初始化变量
# answer = -1
# i = 0
#
# while answer != random_number:
#     answer = int(input("请输入要猜的数字："))
#     i += 1
#     if answer > random_number:
#         print("大了")
#     elif answer < random_number:
#         print("小了")
#     else:
#         print("恭喜猜对了！共猜了%d次。"%(i))

# 更好的写法
i = 0

while True:
    answer = int(input("请输入要猜的数字："))
    i += 1
    if answer > random_number:
        print("大了")
    elif answer < random_number:
        print("小了")
    else:
        print("恭喜猜对了！共猜了%d次。"%(i))
        break