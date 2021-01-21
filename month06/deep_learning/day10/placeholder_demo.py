"""
占位符使用示例
占位符: 替变量占位置, 没有初始化, 没有数据, 执行包含占位符的操作必须
传入数据, 通常用于从数据集中读取的数据占位
"""
import tensorflow as tf

plhd = tf.placeholder(tf.float32, # 类型
                      [2, 3]) # 2行3列张量
plhd2 = tf.placeholder(tf.float32, # 类型
                      [None, 3]) # N行3列张量

with tf.Session() as sess:
    d =  [[1, 2, 3],
          [4, 5, 6]]
    print(sess.run(plhd, feed_dict={plhd: d}))
    print(sess.run(plhd2, feed_dict={plhd2: d}))