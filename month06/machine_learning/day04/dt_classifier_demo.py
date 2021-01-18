import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
raw_samples = []
with open('../data/car.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '') # 去掉换行符
        raw_samples.append(line.split(','))
data = np.array(raw_samples).T # 先转数组, 转置
# print(data.shape)

# 对样本进行标签编码
encoders = [] # 记录所有的标签编码器
train_x = [] # 编码后的数据

for row in range(len(data)):
    encoder = sp.LabelEncoder() # 创建标签编码器
    encoders.append(encoder)
    if row < len(data) - 1: # 不是最后一列
        # 取出第i行执行标签编码
        lbl_code = encoder.fit_transform(data[row])
        train_x.append(lbl_code) # 特征, 存入train_x
    else: # 最后一列:
        # 最后一列为标签, 存入train_y中
        train_y = encoder.fit_transform(data[row])
train_x = np.array(train_x).T
train_y = np.array(train_y)
print(train_x.shape)
print(train_y.shape)

# 创建模型
model = se.RandomForestClassifier(
    max_depth=8, # 最大深度
    n_estimators=150, # 树数量
    random_state=7) # 随机种子
model.fit(train_x, train_y)
print('accuracy:', model.score(train_x, train_y))

# 预测
## 待预测数据
data = [['high', 'med', '5more', '4', 'big', 'low'],
        ['high', 'high', '4', '4', 'med', 'med'],
        ['low', 'low', '2', '2', 'small', 'high'],
        ['low', 'med', '3', '4', 'med', 'high']]

data = np.array(data).T # 转置
test_x = [] # 存放编码后的数据
for row in range(len(data)):
    encoder = encoders[row] # 取得每列使用的标签编码器
    test_x.append(encoder.fit_transform(data[row]))
test_x = np.array(test_x).T # 转置回来

pred_test_y = model.predict(test_x) # 使用测试数据预测
print(pred_test_y)
# 将预测结果反向转换
result = encoders[-1].inverse_transform(pred_test_y)
print(result)
