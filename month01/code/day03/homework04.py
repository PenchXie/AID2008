"""
    累加数字
"""
# 累加0 1 2 3
i = 0
total = 0
while i < 4:
    total += i
    i += 1
print(total)

# 累加2 3 4 5 6
i = 2
total = 0
while i < 7:
    total += i
    i += 1
print(total)

# 累加1 3 5 7
i = 1
total = 0
while i < 9:
    total += i
    i += 2
print(total)

# 累加8 7 6 5 4
i = 8
total = 0
while i > 3:
    total += i
    i -= 1
print(total)

# 累加-1 -2 -3 -4 -5
i = -1
total = 0
while i > -6:
    total += i
    i -= 1
print(total)