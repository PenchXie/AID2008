"""
绘制最优外接椭圆
"""
import cv2
import numpy as np

im = cv2.imread('../data/cloud.png')
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('im_gray', im_gray)
# 二值化
ret, im_bin = cv2.threshold(im_gray, 127, 255, cv2.THRESH_BINARY)
# 检测轮廓
img, cnts, hie = cv2.findContours(
    im_bin, # 原图
    cv2.RETR_EXTERNAL, # 只检测外部轮廓
    cv2.CHAIN_APPROX_NONE) # 保存所有点的坐标数据
# 根据轮廓数据, 产生外接椭圆定位信息
ellipse_data = cv2.fitEllipse(cnts[0])
# 根据椭圆定位信息绘制轮廓
cv2.ellipse(im, # 原图
            ellipse_data, # 椭圆定位信息
            (0, 0, 255), 2) # 线条颜色, 粗细

cv2.imshow('result', im)

cv2.waitKey()
cv2.destroyAllWindows()