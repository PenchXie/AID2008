"""
分类器评估指标 示例
查准率(precision): 衡量查的准不准
召回率(recll): 衡量查的全不全, 又称查全率
F1: 查准率和召回率综合评价指标
"""

# 混淆矩阵示例
import numpy as np
import sklearn.model_selection as ms
import sklearn.metrics as sm
import sklearn.naive_bayes as nb

# 输入，输出
x, y = [], []

# 读取数据文件
with open("../data/multiple1.txt", "r") as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(",")]
        x.append(data[:-1])  # 输入样本：取从第一列到导数第二列
        y.append(data[-1])  # 输出样本：取最后一列

# 样本转数组
x = np.array(x)
y = np.array(y, dtype=int)

# 划分训练集与测试集
train_x, test_x, train_y, test_y = ms.train_test_split(
    x, y,  # 样本输入, 输出
    test_size=0.25,  # 测试集大小
    random_state=7)  # 随机种子, 产生随机数
print(train_x.shape)
print(test_x.shape)

model = nb.GaussianNB()
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)

# 打印召回率, 查准率, F1
recall = sm.recall_score(test_y,  # 真实y值
                         pred_test_y,  # 预测y值
                         average='macro')  # 计算均值不考虑样本的权重
print('recall:', recall)

precision = sm.precision_score(test_y, pred_test_y, average='macro')
print('precision', precision)

print('F1:', sm.f1_score(test_y, pred_test_y, average='macro'))
print('混淆矩阵:')
print(sm.confusion_matrix(test_y, pred_test_y))