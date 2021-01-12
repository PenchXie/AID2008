"""
独热编码示例
"""
import numpy as np
import sklearn.preprocessing as sp

raw_sample = np.array([[1, 3, 2],
                       [7, 5, 4],
                       [1, 8, 6],
                       [7, 3, 9]])
one_hot_encoder = sp.OneHotEncoder(
    sparse=False, # 是否采用稀疏格式
    dtype="int32", # 类型
    categories="auto") # 自动编码
# 正向转换
oh_sample = one_hot_encoder.fit_transform(raw_sample)
print(oh_sample)
# 逆向转换
print(one_hot_encoder.inverse_transform(oh_sample))