"""
查找, 绘制轮廓示例(先查找返回轮廓数据, 再绘制)
"""
import cv2
import numpy as np

im = cv2.imread('../data/3.png')
cv2.imshow('im', im)
# 灰度化
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# 二值化
ret, im_bin = cv2.threshold(im_gray, 127, 255, cv2.THRESH_BINARY)
# 查找轮廓
# cnts: 轮廓数据, 类型是list, list中包含N个ndarray子元素, 每个数组为一个轮廓
#       每个轮廓是一个三维数组
img, cnts, hie = cv2.findContours(
    im_bin, # 在该图像上查找轮廓
    cv2.RETR_EXTERNAL, # 只查找外部轮廓
    cv2.CHAIN_APPROX_NONE) # 存储所有轮廓点
# print(type(cnts)) # list
# for cnt in cnts:
#     # print(type(cnt)) # numpy.ndarry
#     print(cnt.shape)

# 绘制轮廓
im_cnt = cv2.drawContours(
    im, # 在哪一张图像上绘制
    cnts, # 轮廓数据
    -1, # 要绘制的轮廓的索引, -1表示所有轮廓
    (0, 0, 255), # 轮廓颜色
    2) # 轮廓粗细
cv2.imshow('cm_cnt', im_cnt)

cv2.waitKey()
cv2.destroyAllWindows()