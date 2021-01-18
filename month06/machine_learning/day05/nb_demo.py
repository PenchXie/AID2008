"""
朴素贝叶斯分类示例
朴素贝叶斯: 利用贝叶斯定理计算属于每个类别的概率划分到概率最大的类别
朴素指事件之间是独立的
"""
import numpy as np
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp

x, y = [], []  # 输入, 输出
with open('../data/multiple1.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y, dtype=int) # 所属类别为整数

# 定义模型(高斯朴素贝叶斯分类器, 用于连续属性)
model = nb.GaussianNB()
model.fit(x, y) # 训练

# 计算显示范围
left = x[:, 0].min() - 1
right = x[:, 0].max() + 1
h = 0.005

buttom = x[:, 1].min() - 1
top = x[:, 1].max() + 1
v = 0.005

grid_x, grid_y = np.meshgrid(np.arange(left, right, h),
                             np.arange(buttom, top, v))

mesh_x = np.column_stack((grid_x.ravel(), grid_y.ravel()))
mesh_z = model.predict(mesh_x)
mesh_z = mesh_z.reshape(grid_x.shape)

mp.figure('Naive Bayes Classification', facecolor='lightgray')
mp.title('Naive Bayes Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x, grid_y, mesh_z, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=80)
mp.show()