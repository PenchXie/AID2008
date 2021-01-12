"""
模型训练, 保存
"""
import numpy as np
import sklearn.linear_model as lm
import pickle

train_x = np.array([[0.5], [0.6], [0.8], [1.1], [1.4]])  # 输入集
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])  # 输出集
#
# model = lm.LinearRegression()
# model.fit(train_x, train_y)
# print('训练完成')
#
# # 保存模型
# with open('linear_model.pkl', 'wb') as f:
#     pickle.dump(model, f) # 将模型数据存入f中
#     print('模型保存成功')
# 创建线性回归器
model = lm.LinearRegression()
# 用已知输入、输出数据集训练回归器
model.fit(train_x, train_y)

print("训练完成.")

# 保存训练后的模型
with open('linear_model.pkl', 'wb') as f:
    pickle.dump(model, f)
    print("保存模型完成.")