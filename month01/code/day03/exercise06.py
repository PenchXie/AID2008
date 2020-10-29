"""
    选择语句练习
"""
# 输入心理年龄和实际年龄
MA = int(input("请输入心理年龄："))
CA = int(input("请输入实际年龄："))

# 计算智商
IQ = MA / CA * 100

# # 输出结果
# if IQ >= 140:
#     print("天才")
# elif 120 <= IQ <= 139:
#     print("超常")
# elif 110 <= IQ <= 119:
#     print("聪慧")
# elif 90 <= IQ <= 109:
#     print("正常")
# elif 80 <= IQ <= 89:
#     print("迟钝")
# elif IQ < 80:
#     print("低能")
# else:
#     print("不正常")

# 更好的写法
if IQ >= 140:
    print("天才")
elif IQ >= 120:
    print("超常")
elif IQ >= 110:
    print("聪慧")
elif IQ >= 90:
    print("正常")
elif IQ >= 80:
    print("迟钝")
elif IQ < 80:
    print("低能")
else:
    print("不正常")