"""
    列表推导式嵌套练习
"""
result_list = [{i, j} for i in range(1, 7) for j in range(1, 7)]
# result_set = set({})
# for i in range(1, 7):
#     for j in range(1, 7):
#         result_set.add({i, j})
# result_set = set(result_list)
print(result_list)
# print(result_set)