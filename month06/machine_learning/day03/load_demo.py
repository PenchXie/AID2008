"""
模型加载, 使用示例
"""
import numpy as np
import sklearn.linear_model as lm
import pickle
import matplotlib.pyplot as mp

train_x = np.array([[0.5], [0.6], [0.8], [1.1], [1.4]])  # 输入集
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])  # 输出集

# # 加载模型
# with open('linear_model.pkl', 'rb') as f:
#     model = pickle.load(f) # 从f文件对象加载模型
#     print("加载模型完成")

# 加载模型
with open('linear_model.pkl', 'rb') as f:
    model = pickle.load(f)
    print("加载模型完成.")


pred_y = model.predict(train_x)

mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, c='blue', alpha=0.8, s=60, label='Sample')

mp.plot(train_x, pred_y, c='orangered', label='Regression')

mp.legend()
mp.show()