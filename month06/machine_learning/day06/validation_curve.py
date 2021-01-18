"""
验证曲线:验证不同参数下模型的性能
利用验证曲线验证随机森林不同树棵数性能差异
"""
# 验证曲线示例
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp

data = []
with open("../data/car.txt", "r") as f:
    for line in f.readlines():
        data.append(line.replace("\n", "").split(","))

data = np.array(data).T  # 转置
encoders, train_x = [], []

# 对样本数据进行标签编码
for row in range(len(data)):
    encoder = sp.LabelEncoder()  # 创建标签编码器
    encoders.append(encoder)
    if row < len(data) - 1:  # 不是最后一行，为样本特征
        lbl_code = encoder.fit_transform(data[row])  # 编码
        train_x.append(lbl_code)
    else:  # 最后一行，为样本输出
        train_y = encoder.fit_transform(data[row])

train_x = np.array(train_x).T  # 转置回来，变为编码后的矩阵
# print(train_x)

# 定义模型
model = se.RandomForestClassifier(
    max_depth=8, # 树最大深度
    random_state=7) # 随机种子
# 产生一个数组, 值50-500之间
n_estimators = np.arange(50, 550, 50)
# 验证曲线
train_scores1, test_scores1 = ms.validation_curve(
    model, # 模型
    train_x, train_y, # 样本
    'n_estimators', # 待验证参数
    n_estimators, # 待验证参数取值
    cv=5) # 折叠数量
# print(train_scores1)
# print(test_scores1)

# 求每个参数训练结果的均值
train_mean = train_scores1.mean(axis=1)
test_mean = test_scores1.mean(axis=1)
print('train_mean:', train_mean)
print('test_mean:', test_mean)

# 可视化
mp.figure('validation curve')
mp.title('validation curve')
mp.xlabel('n_estimators', fontsize=14)
mp.ylabel('F1 core', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# mp.plot(n_estimators, train_mean, 'o-', c='blue', label='train_mean')
mp.plot(n_estimators, test_mean, ':', c='red', label='test_mean')

mp.show()