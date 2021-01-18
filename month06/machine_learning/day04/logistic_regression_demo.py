"""
逻辑回归示例
逻辑回归: 二分类问题, 先利用回归模型计算数值, 再利用逻辑函数转换为0或1输出
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp

x = np.array([[3, 1], [2, 5], [1, 8], [6, 4],
              [5, 2], [3, 5], [4, 7], [4, -1]])  # 输入
y = np.array([0, 1, 1, 0, 0, 1, 1, 0])  # 标签(类别)

# 定义模型
model = lm.LogisticRegression()  # 逻辑回归模型
model.fit(x, y)  # 训练
test_x = np.array([[3, 9], [6, 1]])
test_y = model.predict(test_x)  # 预测
print(test_y)

# 可视化
## 计算边界
left = x[:, 0].min() - 1 # 计算左边界
right = x[:, 0].max() + 1 # 计算右边界
buttom = x[:, 1].min() - 1 # 下边界
top = x[:, 1].max() + 1 # 上边界

## 生成网格矩阵
grid_x, grid_y = np.meshgrid(
    np.arange(left, right, 0.01), # 产生一组x坐标
    np.arange(buttom, top, 0.01)) # 产生一组y坐标
print(grid_x)
# print(grid_x.shape)
print(grid_y)
# print(grid_y.shape)
## 合并生成的点的x, y坐标
mesh_x = np.column_stack((grid_x.ravel(), grid_y.ravel()))
# print(mesh_x.shape)
# 将每个点坐标送入模型执行预测
mesh_z = model.predict(mesh_x) # mesh_z是每个点的类别
print(mesh_z.shape)
mesh_z = mesh_z.reshape(grid_x.shape) # 还原成二维
print(mesh_z.shape)

mp.figure('Logistic Regression', facecolor='lightgray')
mp.title('Logistic Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x, grid_y, mesh_z, cmap='gray')
mp.scatter(x[:, 0],  # 样本x坐标
           x[:, 1],  # 样本y坐标
           c=y, cmap='brg', s=80)
mp.scatter(test_x[:, 0],  # 样本x坐标
           test_x[:, 1],  # 样本y坐标
           c=test_y, cmap='brg', s=80, marker='D')
mp.show()