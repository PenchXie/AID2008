"""
模糊化处理
"""
import numpy as np
import cv2

im = cv2.imread('../data/lena.jpg', 0)
cv2.imshow('im', im)

# 中值滤波(取邻域内的中位数, 对椒盐噪声抑制效果较好)
im_med = cv2.medianBlur(im,  # 原图
                        5)  # 滤波器大小
cv2.imshow('im_med', im_med)

# 均值模糊
im_mean = cv2.blur(im,  # 原图
                   (3, 3))  # 滤波器大小
cv2.imshow('im_mean', im_mean)

# 高斯模糊
im_gaussian = cv2.GaussianBlur(im,  # 原图
                               (5, 5),  # 滤波器大小
                               3)  # 标准差
cv2.imshow('im_gaussian', im_gaussian)

cv2.waitKey()
cv2.destroyAllWindows()
