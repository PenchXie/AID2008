"""
噪声密度聚类算法示例
"""
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import sklearn.metrics as sm

# 读取样本
x = [] # 输入(聚类问题样本没有输出)
with open('../data/perf.txt', 'r') as f:
    for line in f.readlines():
        line.replace('\n', '')
        data = [float(substr) for substr in line.split(',')]
        x.append(data)
x = np.array(x)

model = sc.DBSCAN(eps=0.8, # 邻域半径
                  min_samples=5) # 最小样本数
model.fit(x) # 训练
pred_y = model.labels_ # 获取训练结果
# print(pred_y)

# 区分核心样本, 噪声样本, 边缘样本
core_mask = np.zeros(len(x), dtype=bool)
# 根据核心样本的索引, 设置为True
core_mask[model.core_sample_indices_] = True

# 挑选噪声样本
offset_mask = (pred_y == -1) # 噪声样本
# print(offset_mask)
# ~符号表示取非
periphery_mask = ~(core_mask|offset_mask) # 边缘样本

# 计算并打印轮廓系数
score = sm.silhouette_score(x, # 样本
                            pred_y, # 标签
                            sample_size=len(x), # 样本数量
                            metric="euclidean")  # 欧式距离度量
print(score)

# 可视化
mp.figure('DBSCAN Cluster', facecolor='lightgray')
mp.title('DBSCAN Cluster', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=14)
mp.grid(linestyle=':')
labels = set(pred_y)
print(labels)
cs = mp.get_cmap('brg', len(labels))(range(len(labels)))
print("cs:", cs)

# 核心点
mp.scatter(x[core_mask][:, 0],  # x坐标值数组
           x[core_mask][:, 1],  # y坐标值数组
           c=cs[pred_y[core_mask]],
           s=80, label='Core')
# 边界点
mp.scatter(x[periphery_mask][:, 0],
           x[periphery_mask][:, 1],
           edgecolor=cs[pred_y[periphery_mask]],
           facecolor='none', s=80, label='Periphery')
# 噪声点
mp.scatter(x[offset_mask][:, 0],
           x[offset_mask][:, 1],
           marker='D', c=cs[pred_y[offset_mask]],
           s=80, label='Offset')
mp.legend()
mp.show()