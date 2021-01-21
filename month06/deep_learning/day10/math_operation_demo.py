"""
数学计算
"""
import tensorflow as tf

# 定义两个张量
x = tf.constant([[1, 2],
                 [3, 4]],
                dtype=tf.float32)
y = tf.constant([[4, 3],
                 [3, 2]],
                dtype=tf.float32)
x_mul_y = tf.matmul(x, y) # 矩阵规则相乘
log_x = tf.log(x) # 求对数

# reduce_xxx: 指定维度上计算
x_sum = tf.reduce_sum(x, axis=[1]) # 1-行方向 0-列方向

# segment_sum: 沿张量的片段计算总和
# 函数返回的是一个Tensor,它与data有相同的类型,与data具有相同的形状
# 但大小为 k(段的数目)的维度0除外
data = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=tf.float32)
segment_ids = tf.constant([0, 0, 0, 1, 1, 2, 2, 2, 2, 2], dtype=tf.int32)
x_seg_sum = tf.segment_sum(data, segment_ids)  # [6, 9, 40]

with tf.Session() as sess:
    print(x_mul_y.eval())
    print(log_x.eval())
    print(x_sum.eval())
    print(x_seg_sum.eval())