import numpy as np

arr = np.arange(10)
print(arr)

arr[2:4] = 13, 14
print(arr)
arr2 = np.arange(12).reshape(3, 4)
print(arr2)
print(arr2[0:2, 1:3])
print(arr2[0:2])
print(arr2[:, 1:3])
