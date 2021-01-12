"""
范围缩放: 经过处理后, 最小值转换为0, 最大值转换为1, 其他值位于0~1之间
"""
import numpy as np
import sklearn.preprocessing as sp

# 定义样本数据
raw_sample = np.array([[1.0, 2.0, 3.0],
                       [4.0, 5.0, 6.0],
                       [7.0, 8.0, 9.0]]).astype("float64")
mms_sample = raw_sample.copy()  # 复制数据
for col in mms_sample.T:  # 循环便利每列
    col_min = col.min()  # 求最小值
    col_max = col.max()  # 求最大值
    col -= col_min  # 减去最小值
    col /= (col_max - col_min)  # 除以(max - min)

print(mms_sample)  # 打印结果
print("==================")
# sklearn提供的API实现
# 先定义对象
mms = sp.MinMaxScaler(feature_range=(0, 1))
print(mms)
# 再进行转换
mms_sample  = mms.fit_transform(raw_sample)
print(mms_sample)
