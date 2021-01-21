"""
多边形拟合几何形状
"""
import numpy as np
import cv2

im = cv2.imread("../data/cloud.png")
cv2.imshow("im", im)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# 提取图像轮廓
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 查找轮廓
img, contours, hierarchy = cv2.findContours(binary,
                                            cv2.RETR_LIST,
                                            cv2.CHAIN_APPROX_NONE)
# 精度一拟合
adp = im.copy()  # 拷贝图像
epsilon = 0.005 * cv2.arcLength(contours[0], True)  # 计算周长, 并根据周长计算精度
approx_data = cv2.approxPolyDP(contours[0],  # 轮廓
                               epsilon,  # 精度
                               True)  # 是否封闭
print(len(approx_data))
print(type(approx_data)) # ndarray
print(type([approx_data])) # list
adp = cv2.drawContours(adp,
                       [approx_data], # []将数组包成列表
                       0, (0, 0, 255), 2) # 绘制多边形
cv2.imshow('epsilon1', adp)

cv2.waitKey()
cv2.destroyAllWindows()
