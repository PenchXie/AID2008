"""
多项式回归示例
多项式回归实现: 先做多项式扩展, 再做线性回归
"""
import numpy as np
import sklearn.linear_model as lm
import sklearn.metrics as sm  # 性能评估
import matplotlib.pyplot as mp
import sklearn.pipeline as pl  # 管线
import sklearn.preprocessing as sp

# 1. 从样本文件读取数据
train_x, train_y = [], []  # 输入, 输出
with open('../data/poly_sample.txt', 'rt') as f:
    for line in f.readlines():  # 遍历每一行
        data = [float(substr) for substr in line.split(', ')]
        train_x.append(data[:-1])  # 取第一至倒数第二个字段
        train_y.append(data[-1])  # 取最后一列
# 将列表转换为数组
train_x = np.array(train_x)
train_y = np.array(train_y)
# print(train_x.shape)
# print(train_y.shape)
# 2. 构建模型, 训练模型
model = pl.make_pipeline( #　管线，　将两个模型连接到一起
    sp.PolynomialFeatures(3), # 多项式特征扩展, 最高次数3
    lm.LinearRegression()) # 线性回归器, 求解

model.fit(train_x, train_y) # 训练

pred_train_y = model.predict(train_x) # 预测
# print(pred_train_y) # 打印预测结果

# 打印模型R2评估系数
r2 = sm.r2_score(train_y, pred_train_y)
print('R2:', r2)

# 3. 可视化
test_x = np.linspace(train_x.min(), train_x.max(), 1000) # 产生等距离的1000个数字
pre_test_y = model.predict(test_x.reshape(-1, 1))
# print(test_x.reshape(-1, 1).shape)
mp.figure('Polynomial Regression')
mp.title('Polynomial Regression')
mp.xlabel('x', fontsize=14)
mp.ylabel('x', fontsize=14)
mp.tick_params(labelsize=10) # 刻度字体大小
mp.grid(linestyle=':')
# 样本散点图
mp.scatter(train_x, train_y, c='blue', label='samples')
# 绘制多项式模型曲线图
mp.plot(test_x, pre_test_y, c='orangered', label='Polynomial')
mp.legend()
mp.show()