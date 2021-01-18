"""
考虑样本的连续性聚类示例
"""
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import sklearn.neighbors as nb

# 构造样本(阿基米德螺线)
n_sample = 500  # 样本数量
t = 2.5 * np.pi * (1 + 2 * np.random.rand(n_sample, 1))  # 产生随机角度

# 计算螺线样本
x = 0.05 * t * np.cos(t)
y = 0.05 * t * np.sin(t)
n = 0.05 * np.random.rand(n_sample, 2)  # 产生随机噪声
x = np.hstack((x, y)) + n  # 合并, 并加入噪声
print(x.shape)

# 使用凝聚层次算法聚类(不考虑连续性)
# model = sc.AgglomerativeClustering(n_clusters=3,
#                                    linkage='average')  # 距离平均值作为度量两个聚簇间距离的依据
# model.fit(x)
# pred_y1 = model.labels_  # 取出聚类结果

# 定义凝聚层次算法模型(考虑连续性)
conn = nb.kneighbors_graph( # 创建每个样本的临近集合
    x, # 样本
    10, # 临近样本数量
    include_self=False) # 是否包含自己
model = sc.AgglomerativeClustering(
    n_clusters=3, linkage='average',
    # 在凝聚过程中, 首先考虑临近集合中连续性较好的样本
    connectivity=conn)
model.fit(x)
pred_y1 = model.labels_
# 可视化
mp.figure("AgglomerativeClustering Cluster", facecolor="lightgray")
mp.title("AgglomerativeClustering Cluster")
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.axis("equal")
mp.scatter(x[:, 0], x[:, 1], c=pred_y1, cmap="brg", s=80, alpha=0.5)
mp.show()
