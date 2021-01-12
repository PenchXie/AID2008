import numpy as np
# sort
# data = np.array([2, 5, 6, 9, 1, 8, 7])
# data.sort()
# print(data)
# argsort
# data_sort = data.argsort()
# print(data_sort)
# data2 = np.array([[1, 5, 2, 7],
#                   [4, 8, 3, 6],
#                   [7, 8, 11, 10]])
# data2.sort(axis=1)
# data2.sort(axis=0)
# print(data2)
arr = np.arange(20).reshape(4, 5)
print(arr)
# print(arr.sum())
# print(arr.mean(axis=1))
# print(arr.mean(axis=0))
# print(arr.std())
print(arr.cumsum())
data = np.cumsum(arr, axis=0)
print(data)
print(arr.cumprod())
data_2 = np.cumprod(arr, axis=0)
print(data_2)