# 将列表中所有奇数设置为None
list01 = list(range(10))
print(list01)

for i, num in enumerate(list01):
    if num % 2:
        list01[i] = None

print(list01)

list02 = list(range(10))
print(list02)
for i, num in enumerate(list02):
    if num % 2 == 0:
        list02[i] += 1
print(list02)
