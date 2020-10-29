"""
    定义函数,将列表中奇数删除
"""
list01 = [3, 7, 5, 6, 7, 8, 9, 13]

# 删除奇数
def del_odd_nums(int_list):
    """
    将输入整形列表中奇数删除
    :param int_list: 列表, 元素应全为int型数据
    :return: 返回删除奇数后的列表
    """
    for i in range(len(int_list) - 1, -1, -1):
        if int_list[i] % 2:
            del int_list[i]
    return int_list


# 提取偶数
def get_even_nums(int_list):
    int_list = [num for num in int_list if num % 2 == 0]
    return int_list


print(del_odd_nums(list01))
print(get_even_nums(list01))
