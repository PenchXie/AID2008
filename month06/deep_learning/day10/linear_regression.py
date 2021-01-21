"""
利用tensorflow实现线性回归
"""
import tensorflow as tf

# 第一步: 准备数据
x = tf.random_normal([100, 1],  # 形状
                     mean=1.75,  # 均值
                     stddev=0.5,  # 标准差
                     name='x_data')  # 张量名称
y = tf.matmul(x, [[2.0]]) + 5.0  # 计算y = 2x + 5

# 第二步: 建立模型, 执行预测
w = tf.Variable(tf.random_normal([1, 1], name='w'))  # 权重
b = tf.Variable(0.0, name='b')  # 偏置
y_predict = tf.matmul(x, w) + b  # 计算xw + b

# 第三步: 定义损失函数, 优化器
## 定义均方差损失函数
loss = tf.reduce_mean(tf.square(y - y_predict))
train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

## 指定收集的张量
tf.summary.scalar('losses', loss)  # 指定收集loss操作的值

# 第四步: 迭代训练
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())  # 初始化
    # 定义FileWriter对象, 用于写事件文件
    fw = tf.summary.FileWriter('/home/tarena/summary/', graph=sess.graph)

    for i in range(500):
        sess.run(train_op)  # 反复执行损失函数优化操作
        print('%d: w=%f, b=%f, loss=%f' % (i, w.eval(), b.eval(), loss.eval()))
        # 完成一次训练, 收集损失函数的值
        summary = sess.run(tf.summary.merge_all())  # 收集, 合并数据
        fw.add_summary(summary, i)  # 第i次写入事件文件

# 第五步: 预测(本示例没有)
