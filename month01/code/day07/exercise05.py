"""
    对数字列表进行升序排列（小 --> 大）
"""
num_list = list(range(9, -1, -1))

for i in range(len(num_list) - 1):
    for j in range(i + 1, len(num_list)):
        if num_list[i] > num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

print(num_list)