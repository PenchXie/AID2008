"""
透视变换示例(用于图像形状矫正)
"""
import cv2
import numpy as np

im = cv2.imread('../data/pers.png', 0)

cv2.imshow('im', im)
# # 二值化
# t, im = cv2.threshold(im, 180, 255, cv2.THRESH_BINARY)

h, w = im.shape[:2]  # 取出高度, 宽度

# 定义透视变换原点坐标, 目标点坐标
pts1 = np.float32([[58, 2], [167, 9], [8, 196], [126, 196]])  # 输入图像四个顶点坐标
pts2 = np.float32([[16, 2], [167, 8], [8, 196], [169, 196]])  # 输出图像四个顶点坐标
# 生成透视变换矩阵
M = cv2.getPerspectiveTransform(pts1,  # 原顶点
                                pts2)  # 目标顶点
print(M.shape)
dst = cv2.warpPerspective(im,  # 原图
                          M,  # 透视变换矩阵
                          (w, h))  # 输出图像高度, 宽度
cv2.imshow('dst', dst)

# 将矩形矫正为平行四边形
M = cv2.getPerspectiveTransform(pts2,  # 原顶点
                                pts1)  # 目标顶点

dst2 = cv2.warpPerspective(dst,  # 原图
                           M,  # 透视变换矩阵
                           (w, h))  # 输出图像高度, 宽度
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()
