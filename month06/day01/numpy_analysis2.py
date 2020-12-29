"""
use numpy to read or write files
"""
import numpy as np

arr = np.arange(100).reshape(10, 10)
# print(arr)
# np.save(file='arr100', arr=arr)
# load_data = np.load('arr100.npy')
# print(load_data)
arr1 = np.array([1, 2, 3, 4])
# np.savez('two_arrays', arr, arr1)
load_data2 = np.load('two_arrays.npz')
print(load_data2.files)
print(load_data2['arr_0'])
print(load_data2['arr_1'])