"""
    for循环累加练习
    for + range函数
"""
# 累加0 1 2 3
total = 0
for i in range(4):
    total += i
print(total)

# 累加2 3 4 5 6
total = 0
for i in range(2, 7):
    total += i
print(total)

# 累加1 3 5 7
total = 0
for i in range(1, 9, 2):
    total += i
print(total)

# 累加8 7 6 5 4
total = 0
for i in range(8, 3, -1):
    total += i
print(total)

# 累加-1, -2, -3, -4, -5
total = 0
for i in range(-1, -6, -1):
    total += i
print(total)
