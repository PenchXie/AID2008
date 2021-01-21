"""
张量形状改变
张量形状:
    静态形状: 主要用于存储, 要求稳定, 一旦设置就不能再改变, 不能跨阶设置
    动态形态: 主要用于计算, 要求灵活, 可以多次设置, 可以跨阶设置
"""
import tensorflow as tf

pld = tf.placeholder(tf.float32, [None, 3])
print(pld) # 打印对象信息

pld.set_shape([4, 3])
print(pld)

# pld.set_shape([3, 3]) # 报错, 静态形状一旦设置就不能改变

new_pld = tf.reshape(pld, [3, 4]) # 动态形状
print(new_pld)
new_pld2 = tf.reshape(pld, [2, 6])
print(new_pld2)

# new_pld3 = tf.reshape(pld, [2, 4]) # 报错, 元素个数不符
