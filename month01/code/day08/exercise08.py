"""
    定义函数，将列表中大于某个值的元素设置为None
"""
def set_list_none(target_list, value):
    for i in range(len(target_list)):
        if target_list[i] > value:
            target_list[i] = None

list01 = [34, 545, 56, 7, 78, 8]
# set_list_none(list01, 10)
set_list_none(list01, 100)
print(list01)
