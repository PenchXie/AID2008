"""
图像锐化(放大像素之间的差异)
"""
import numpy as np
import cv2

im = cv2.imread('../data/lena.jpg', 0)
cv2.imshow('im', im)

# 定义锐化算子
sharpen_1 = np.array([[-1, -1, -1],
                      [-1, 9, -1],
                      [-1, -1, -1]])
im_sharpen1 = cv2.filter2D(im, # 原图
                           -1, # 深度, -1表示所有通道
                           sharpen_1) # 滤波器
cv2.imshow('im_sharpen1', im_sharpen1)

# 锐化算子2
sharpen_2 = np.array([[0, -1, 0],
                      [-1, 8, -1],
                      [0, 1, 0]]) / 4.0
im_sharpen2 = cv2.filter2D(im, # 原图
                           -1, # 深度, -1表示所有通道
                           sharpen_2) # 滤波器
cv2.imshow('im_sharpen2', im_sharpen2)

cv2.waitKey()
cv2.destroyAllWindows()