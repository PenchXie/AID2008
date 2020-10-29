"""
    while循环练习４, 计算纸对折多少次厚度超过珠穆朗玛峰
"""
# 初始化变量
thickness = 1e-5
i = 0

# 循环
while thickness < 8848.43:
    thickness *= 2
    i += 1

# 输出结果
print("对折%d次超过珠穆朗玛峰"%(i))