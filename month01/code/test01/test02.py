"""
    删除列表中所有重复的元素
"""


def del_repeat_elements(target_list):
    for i in range(len(target_list) - 1, -1, -1):
        if target_list[i] in target_list[:i]:
            del target_list[i]
        # 索引写法
        # for j in range(i):
        #     if target_list[i] == target_list[j]:
        #         del target_list[i]


list01 = [4, 35, 7, 64, 7, 35, 4, 35, 7, 64, 7, 35, 4, 35, 7, 64, 7, 35, 4, 35, 7, 64, 7, 35]
del_repeat_elements(list01)
print(list01)
