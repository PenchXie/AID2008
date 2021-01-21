"""
变量使用示例(变量使用之前要初始化)
"""
import tensorflow as tf

a = tf.constant([1, 2, 3, 4, 5])

var = tf.Variable(tf.random_normal([2, 3]), name='var1')

# 定义初始化操作
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op) # 执行初始化
    print(a.eval()) # eval用于有返回值情况, 无返回值则用run; run有无返回值均可使用
    print(var.eval())