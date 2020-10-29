"""
    根据下列代码，创建降序排列函数
"""
list01 = [5, 15, 25, 35, 1, 2]
def descend_order(target_list):
    for r in range(len(target_list) - 1):
        for c in range(r + 1, len(target_list)):
            if target_list[r] < target_list[c]:
                target_list[r], target_list[c] = target_list[c], target_list[r]

descend_order(list01)
print(list01)