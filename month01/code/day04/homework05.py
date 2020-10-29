"""
    输入4个同学年龄, 打印最小年龄
"""
# # 初始化变量
# min_age = 100000
# # 输入年龄
# for i in range(4):
#     age = int(input("请输入第%d位同学年龄:" % (i + 1)))
#     if age < min_age:
#         min_age = age
#
# 输入年龄
age01 = int(input("请输入第一位同学年龄："))
age02 = int(input("请输入第二位同学年龄："))
age03 = int(input("请输入第三位同学年龄："))
age04 = int(input("请输入第四位同学年龄："))

# 假定第一位同学年龄最小
min_age = age01

if age02 < min_age:
    min_age = age02
if age03 < min_age:
    min_age = age03
if age04 < min_age:
    min_age = age04

# 输出结果
print("最小年龄为:%d" % (min_age))