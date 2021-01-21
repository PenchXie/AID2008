"""
图像腐蚀示例
腐蚀核越大, 迭代次数越多, 腐蚀越严重
"""
import cv2
import numpy as np

im = cv2.imread('../data/5.png')
cv2.imshow('im', im)

# 腐蚀
kernel = np.ones((3, 3), np.uint8)
im_erode = cv2.erode(im, # 原图
                     kernel, # 腐蚀核
                     iterations=10) # 迭代次数
cv2.imshow('im_erode', im_erode)

cv2.waitKey()
cv2.destroyAllWindows()