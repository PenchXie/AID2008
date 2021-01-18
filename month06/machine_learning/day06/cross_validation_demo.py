"""
交叉验证示例
交叉验证
1. 数据集样本数量较少情况下使用
2. 将样本划分为k个折叠, 每次使用其中一个作为测试集, 其余折叠作为训练集
"""

# 交叉验证示例
import numpy as np
import sklearn.model_selection as ms
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp

x, y = [], []  # 输入，输出

# 读取数据文件
with open("../data/multiple1.txt", "r") as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(",")]
        x.append(data[:-1])  # 输入样本：取从第一列到导数第二列
        y.append(data[-1])  # 输出样本：取最后一列

train_x = np.array(x)
train_y = np.array(y, dtype=int)

# 定义分类模型, 并采用交叉验证
model = nb.GaussianNB()
# 采用交叉验证计算查准率
pws = ms.cross_val_score(model, # 原始模型
                         train_x, train_y, # 样本
                         cv=5, # 折叠数量
                         scoring='precision_weighted') # 查准率
print('precision:', pws)

# 召回率
rws  = ms.cross_val_score(model, train_x, train_y, cv=5,
                          scoring='recall_weighted') # 召回率
print('recall:', rws)

# f1
f1 = ms.cross_val_score(model, train_x, train_y, cv=5, scoring='f1_weighted')
print('f1:', f1)

# 准确率
acc = ms.cross_val_score(model, train_x, train_y, cv=5, scoring='accuracy')
print('acc:', acc)