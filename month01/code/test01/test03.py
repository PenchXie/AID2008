"""
    判断二维数字列表是否存在某个数字
"""


def if_num_exist(target_list, num):
    for i in range(len(target_list)):
        # for j in range(len(target_list[i])):
        #     if num == target_list[i][j]:
        #         return True
        if num in target_list[i]:
            return True

    return False


list01 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(if_num_exist(list01, 10))
