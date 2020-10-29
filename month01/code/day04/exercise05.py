"""
    跳转语句练习, 累加10-60之间各位不是3/5/8的整数和
"""
# 初始化变量
total = 0

# 循环
for i in range(10, 61):
    unit = i % 10
    if unit == 3 or unit == 5 or unit == 8:
        continue
    total += i

# 输出结果
print(total)