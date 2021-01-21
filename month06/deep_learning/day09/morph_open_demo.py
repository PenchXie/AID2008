"""
图像开运算示例
"""
import cv2
import numpy as np

im1 = cv2.imread('../data/7.png')
im2 = cv2.imread('../data/8.png')

# 开运算
k = np.ones((10, 10), np.uint8)
r1 = cv2.morphologyEx(im1, cv2.MORPH_OPEN, k)
r2 = cv2.morphologyEx(im2, cv2.MORPH_OPEN, k)

cv2.imshow('im1', im1)
cv2.imshow('result1', r1)

cv2.imshow('im2', im2)
cv2.imshow('result2', r2)

cv2.waitKey()
cv2.destroyAllWindows()