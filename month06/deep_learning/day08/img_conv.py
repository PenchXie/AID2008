from scipy import misc, signal
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
im = misc.imread('../data/zebra.png', flatten=True)

# 定义卷积核
flt = np.array([[-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]])

flt2 = np.array([[1, 2, 1],
                 [0, 0, 0],
                 [-1, -2, -1]])

conv_img1 = signal.convolve2d(
    im,  # 原始图像
    flt,  # 卷积核
    boundary='symm',  # 边沿处理方式
    mode='same').astype('int32')  # same表示同维卷积

conv_img2 = signal.convolve2d(
    im,  # 原始图像
    flt2,  # 卷积核
    boundary='symm',  # 边沿处理方式
    mode='same').astype('int32')  # same表示同维卷积

# 显示卷积后的结果
plt.figure('Conv2D')
plt.subplot(131)  # 1行, 3列, 第1个子图
plt.imshow(im, cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(132)
plt.imshow(conv_img1, cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(133)
plt.imshow(conv_img2, cmap='gray')
plt.xticks([])
plt.yticks([])

plt.show()
