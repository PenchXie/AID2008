"""
标签编码示例
标签编码: 将字符串转换为数字, 从而方便计算
"""
import numpy as np
import sklearn.preprocessing as sp

raw_sample = np.array(["audi", "ford", "audi", "bmw", "ford", "bmw"])
lbl_encoder = sp.LabelEncoder() # 定义标签编码器
lbl_sample = lbl_encoder.fit_transform(raw_sample) # 执行编码
print(lbl_sample)
# 逆向编码
print(lbl_encoder.inverse_transform(lbl_sample)) # 打印编码结果
