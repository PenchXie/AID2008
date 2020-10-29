"""
    取最大值算法练习
"""
# # 依次输入四个同学的身高并与最大值进行比较
# height_1 = int(input("请输入第一个同学的身高："))
# max_height = height_1
#
# height_2 = int(input("请输入第二个同学的身高："))
# if height_2 > max_height:
#     max_height = height_2
#
# height_3 = int(input("请输入第三个同学的身高："))
# if height_3 > max_height:
#     max_height = height_3
#
# height_4 = int(input("请输入第四个同学的身高："))
# if height_4 > max_height:
#     max_height = height_4
#
# # 输出最高身高
# print("最高身高为：" + str(max_height))

# 更好的写法, 便于debug, 格式更优
height_1 = int(input("请输入第一个同学的身高："))
height_2 = int(input("请输入第二个同学的身高："))
height_3 = int(input("请输入第三个同学的身高："))
height_4 = int(input("请输入第四个同学的身高："))

# 假设第一个身高最大
max_height = height_1
# 算法
if height_2 > max_height:
    max_height = height_2
if height_3 > max_height:
    max_height = height_3
if height_4 > max_height:
    max_height = height_4
# 输出最高身高
print("最高身高为：" + str(max_height))

# 第二种思路
# max_height02 = 0
# for i in range(1,5):
#     height = int(input("第%d位同学的身高:"%(i)))
#     if height > max_height02:
#         max_height02 = height
#
# print(max_height02)