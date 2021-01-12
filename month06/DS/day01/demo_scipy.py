import numpy as np
from scipy.optimize import leastsq

Xi = np.array([6.19, 2.51, 7.29, 7.01, 5.7, 2.66, 3.98, 2.5, 9.1, 4.2])
Yi = np.array([5.25, 2.83, 6.41, 6.71, 5.1, 4.23, 5.05, 1.98, 10.5, 6.3])


# 定义拟合函数
def func(p, x):
    k, b = p
    return k * x + b


# 定义误差函数
def error(p, x, y, s):
    print(s)
    return func(p, x) - y


# 设置初始值
p0 = [1, 1]
s= 'test the number of iteration'
# 主函数
result = leastsq(error, p0, args=(Xi, Yi, s))
print(result)
k, b = result[0]
print('k=', k, '\n', 'b=', b)
# 预测x=10,y的值
y = k * 10 + b
print(y)
y1 = np.round(y, 2)
print(y1)
