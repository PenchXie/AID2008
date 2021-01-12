"""
利用sklearn库提供的API实现线性回归
对象名称: LinearRegression
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp

# 准备数据
train_x = np.array([[0.5], [0.6], [0.8], [1.1], [1.4]])  # 输入集
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])  # 输出集

# 构建模型, 训练
model = lm.LinearRegression() # 线性回归器
model.fit(train_x, train_y) # 训练
pred_y = model.predict(train_x) # 利用训练集输入预测

## 取出模型的系数
print('coef_:', model.coef_) # 系数
print('intercept_:', model.intercept_) # 截距

# 可视化
mp.figure('Linear Regression') # 创建图形窗体
mp.title('Linear Regression') # 图形名称
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10) # 刻度字体大小
mp.grid(linestyle=':') # 网格线:虚线
## 样本散点
mp.scatter(train_x, train_y, c='blue', s=60, label='samples')
## 绘制拟合的线性模型
mp.plot(train_x, pred_y, c='red', label='Linear')

mp.legend()
mp.show()