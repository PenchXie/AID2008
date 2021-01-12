"""
计算1~10个类别信息熵, 类别越多熵越大(越混乱)
"""
import math
import numpy as np
import matplotlib.pyplot as mp

class_num = 10 # 类别最大数量

# 根据类别数量计算熵
def entropy_calculator(n): # n表示类别数量
    p = 1 / n # 假设每个类别的占比(概率)为1/n
    entropy_value = 0.0

    for i in range(n):
        p_i = p * math.log(p)
        entropy_value += p_i # 累加

    return -entropy_value

# print(entropy_calculator(10000))
entropy_arr = [] # 存放1~n个类别的熵值
for i in range(1, class_num + 1):
    entropy = entropy_calculator(i) # 计算类别数量为i的熵
    entropy_arr.append(entropy) # 记录到列表

# print(entropy_arr)

# 可视化回归曲线
mp.figure('Entropy', facecolor='lightgray')
mp.title('Entropy', fontsize=20)
mp.xlabel('Class Num', fontsize=14)
mp.ylabel('Entropy', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle='-')
x = np.arange(0, 10, 1)
print(x)
mp.plot(x, entropy_arr, c='orangered', label='entropy')

mp.legend()
mp.show()