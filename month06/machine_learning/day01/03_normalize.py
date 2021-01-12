"""
归一化处理示例: 将一行数值转换为0~1百分比, 能更好反映出此消彼长比例变化
"""
import numpy as np
import sklearn.preprocessing as sp

# 样本数据
raw_sample = np.array([[10.0, 20.0, 5.0],
                       [8.0, 10.0, 1.0]])
nor_sample = raw_sample.copy()  # 复制
for row in nor_sample:  # 遍历每行
    row /= abs(row).sum()  # 先求绝对值之和, 再除

print(nor_sample)  # 打印结果

print("===================")
# sklearn提供的API计算
nor_sample = sp.normalize(raw_sample, norm='l1')
print(nor_sample)
