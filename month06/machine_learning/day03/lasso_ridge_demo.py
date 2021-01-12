import numpy as np
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as mp

# 读取数据
x, y = [], []
with open('../data/abnormal.txt', 'rt') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data[:-1]) # 输入
        y.append(data[-1]) # 输出
x = np.array(x)
y = np.array(y)
# print(x.T)

# 分别定义线性回归, Lasso回归, 岭回归模型训练
## 标准线性模型
model = lm.LinearRegression()
model.fit(x, y)
pred_y = model.predict(x)

## 岭回归
model_2 = lm.Ridge(alpha=200, # 正则强度, 该值越大, 异常样本权重越小
                   max_iter=1000) # 最大迭代次数
model_2.fit(x, y)
pred_y2 = model_2.predict(x)

## Lasso回归
model_3 = lm.Lasso(alpha=1, # 正则强度
                   max_iter=1000) # 最大迭代次数
model_3.fit(x, y)
pred_y3 = model_3.predict(x)

# 可视化
mp.figure('Linear & Ridge & Lasso', facecolor='lightgray')
mp.title('Linear & Ridge & Lasso', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, c='dodgerblue', alpha=0.8, s=60, label='Sample')
sorted_idx = x.T[0].argsort()

mp.plot(x[sorted_idx], pred_y[sorted_idx], c='orangered', label='Linear')  # 线性回归
mp.plot(x[sorted_idx], pred_y2[sorted_idx], c='limegreen', label='Ridge')  # 岭回归
mp.plot(x[sorted_idx], pred_y3[sorted_idx], c='blue', label='Lasso')  # Lasso回归

mp.legend()
mp.show()