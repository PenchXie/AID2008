"""
归并排序
"""
def merge_sort(li):
    # 递归出口
    if len(li) == 1:
        # print(li)
        return li
    mid_num = len(li) // 2
    left = li[:mid_num]
    right = li[mid_num:]
    # 递归思想
    left_li = merge_sort(left)
    right_li = merge_sort(right)
    return merge(left_li, right_li)

def merge(left_li, right_li):
    """合并代码"""
    result = []
    while left_li and right_li:
        result.append(left_li.pop(0) if left_li[0] < right_li[0] else right_li.pop(0))
    result += right_li if not left_li else left_li
    return result

if __name__ == '__main__':
    li = [6, 5, 4, 7, 2, 8, 1, 3]
    # print(merge([3, 5], [4, 6]))
    print(merge_sort(li))
