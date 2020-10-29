"""
    二维列表练习
"""
list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
# 将第一行从左到右逐行打印
for i in range(len(list01[0])):
    print(list01[0][i], end=" ")
print()
# 将第二行从右到左逐行打印
for i in range(len(list01[1]) - 1, -1, -1):
    print(list01[1][i], end=" ")
print()
# 将第三列行从上到下逐个打印
for i in range(len(list01)):
    print(list01[i][2], end=" ")
print()
# 将第四列行从下到上逐个打印
for i in range(len(list01) - 1, -1, -1):
    print(list01[i][3], end=" ")
print()
# 将二维列表以表格状打印
for r in range(len(list01)):
    for c in range(len(list01[r])):
        # print("%2d" % list01[r][c], end=" ")
        print(list01[r][c], end="\t")
    print()
