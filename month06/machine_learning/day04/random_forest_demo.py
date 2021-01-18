import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.metrics as sm
import sklearn.ensemble as se

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

# 创建模型
model = se.RandomForestRegressor(
    max_depth=10,
    n_estimators=1000, # 树数量
    min_samples_split=2) # 最小样本数量
model.fit(train_x, train_y) # 训练
pred_test_y = model.predict(test_x) # 预测
# 计算并打印R2值
print(sm.r2_score(test_y, pred_test_y))