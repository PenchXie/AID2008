"""
将图信息写入事件文件, 在tensorboard中使用
"""
import tensorflow as tf

b = tf.constant(3.0, name='a')
c = tf.constant(3.0, name='b')
d = tf.add(b, c, name='my_add')

var = tf.Variable(tf.random_normal([2, 3]), name='var1')

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # 定义FileWriter对象(负责事件文件写入)
    fw = tf.summary.FileWriter(
        '/home/tarena/summary/',
        graph=sess.graph)

    print(sess.run([d, var]))