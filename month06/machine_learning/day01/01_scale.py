"""
均值移除示例
均值移除: 对每列特征进行变换, 变换后均值为0, 标准差为1(数据分布更加规范)
"""
import numpy as np
import sklearn.preprocessing as sp

# 样本数据
raw_sample = np.array([[3.0, -1.0, 2.0],
                       [0.0, 4.0, 3.0],
                       [1.0, -4.0, 2.0]])
std_sample = raw_sample.copy()  # 复制样本
for col in std_sample.T:  # T表示转置, 遍历每列
    col_mean = col.mean()  # 计算每列均值
    # print(col_mean)
    col_std = col.std()  # 计算每列标准差
    col -= col_mean  # 每列减去均值
    col /= col_std  # 每列减去标准差
    # print(col)

print(std_sample)  # 打印均值移除后的样本数据
print(std_sample.mean(axis=0))  # 打印列平均值
print(std_sample.std(axis=0))  # 打印列标准差

# 利用sklearn提供的API实现
std_sample = sp.scale(raw_sample)
print(std_sample)  # 打印均值移除后的样本数据
print(std_sample.mean(axis=0))  # 打印列平均值
print(std_sample.std(axis=0))  # 打印列标准差