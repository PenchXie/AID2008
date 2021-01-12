"""
决策树示例:波士顿房价预测, 根据13个特征预测房屋价格
"""
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.metrics as sm

# 读取数据集
boston = sd.load_boston()
# print(boston.data.shape)
# print(boston.target.shape)

# 样本随机化(打乱)
random_seed = 7 # 随机种子, 用来产生随机数
x, y = su.shuffle(boston.data, boston.target, random_state=random_seed)
# 分训练集, 测试集
train_size = int(len(x) * 0.8) # 计算训练集大小(80%)
train_x = x[:train_size] # 切出前面80%
test_x = x[train_size:] # 切出后面20%

train_y = y[:train_size] # 切出前面80%
test_y = y[train_size:] # 切出后面20%

# 定义模型, 训练模型, 预测
model = st.DecisionTreeRegressor(max_depth=4) # 决策树回归器模型
model.fit(train_x, train_y) # 训练
pred_test_y = model.predict(test_x)

print(sm.r2_score(test_y, pred_test_y)) # 打印R2值

import matplotlib.pyplot as mp
import numpy as np
fi = model.feature_importances_  # 获取特征重要性
print("fi:", fi)

# 特征重要性可视化
mp.figure("Feature importances", facecolor="lightgray")
mp.plot()
mp.title("DT Feature", fontsize=16)
mp.ylabel("Feature importances", fontsize=14)
mp.grid(linestyle=":", axis=1)
x = np.arange(fi.size)
sorted_idx = fi.argsort()[::-1]  # 重要性排序(倒序)
fi = fi[sorted_idx]  # 根据排序索引重新排特征值
mp.xticks(x, boston.feature_names[sorted_idx])
mp.bar(x, fi, 0.4, color="dodgerblue", label="DT Feature importances")

mp.legend()
mp.tight_layout()
mp.show()