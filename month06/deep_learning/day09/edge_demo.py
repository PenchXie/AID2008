"""
提取边沿
"""
import cv2

im = cv2.imread('../data/lily.png', 0)
cv2.imshow('im', im)

# sobel边沿提取
im_sobel = cv2.Sobel(im, # 原图
                     cv2.CV_64F, # 深度, 本来应该是-1, 为了避免错误设置为稍大一些的浮点数
                     1, 1, # 提取水平与垂直两个方向的轮廓
                     ksize=5) # 滤波器大小
cv2.imshow('im_sobel', im_sobel)

# Laplacian边沿提取
im_lap = cv2.Laplacian(im, cv2.CV_64F)
cv2.imshow('im_lap', im_lap)

# canny边沿提取
im_canny = cv2.Canny(im, # 原图
                     100, # 滞后阈值
                     240) #　模糊度
cv2.imshow('im_canny', im_canny)

cv2.waitKey()
cv2.destroyAllWindows()