"""
凝聚层次聚类示例
凝聚层次:
1. 基于层次的聚类算法
2. 事先设定聚类的数量, 不断合并距离最近的聚簇, 知道聚簇的数量等于事先设定的数量
"""
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import sklearn.metrics as sm

# 读取样本
x = [] # 输入(聚类问题样本没有输出)
with open('../data/multiple3.txt', 'r') as f:
    for line in f.readlines():
        line.replace('\n', '')
        data = [float(substr) for substr in line.split(',')]
        x.append(data)
x = np.array(x)

# 定义凝聚聚类模型, n_clusters参数表示聚类数量
model = sc.AgglomerativeClustering(n_clusters=6)
model.fit(x)
pred_y = model.labels_ # 获取聚类结果

# 计算打印轮廓系数
score = sm.silhouette_score(x, # 样本
                            pred_y, # 标签
                            sample_size=len(x), # 样本数量
                            metric="euclidean")  # 欧式距离度量
print('轮廓系数:', score)

# 可视化
mp.figure("Agglomerative", facecolor="lightgray")
mp.title("Agglomerative")
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:, 0], x[:, 1], s=80, c=pred_y, cmap="brg")
mp.show()