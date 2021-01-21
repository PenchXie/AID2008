"""
图像形状矫正
"""
import cv2
import numpy as np
import math

# 读取原图
im = cv2.imread('../data/paper.jpg')
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('im_gray', im_gray)

# # 二值化处理(效果不好)
# t, im_bin = cv2.threshold(im_gray, 200, 255, cv2.THRESH_BINARY)
# cv2.imshow('im_bin', im_bin)

# 模糊, 膨胀合并过细的细节
im_blur = cv2.GaussianBlur(im_gray, (5, 5), 0)
im_dilate = cv2.dilate(im_blur, (3, 3))
cv2.imshow('im_dilate', im_dilate)

# 边沿提取
im_canny = cv2.Canny(im_dilate, 10, 240)
cv2.imshow('im_canny', im_canny)

# 在canny边沿提取结果之上查找外部轮廓
img, cnts, hie = cv2.findContours(
    im_canny, # canny边沿提取结果
    cv2.RETR_EXTERNAL, # 只提取外部轮廓
    cv2.CHAIN_APPROX_SIMPLE) # 简化格式保存轮廓
# for cnt in cnts:
#     print(cnt.shape)

# 绘制轮廓
im_cnt = cv2.drawContours(im, cnts, # 轮廓数据
                          -1, #绘制所有轮廓
                          (0, 0, 255), 2) # 颜色，　粗细
cv2.imshow('im_cnt', im_cnt)

# 计算轮廓面积，　由大到小排序
if len(cnts) > 0: # 轮廓数量大于0
    # 排序
    cnts = sorted(cnts, # 待排序容器
                  key=cv2.contourArea, # 排序依据: 面积
                  reverse=True)
    # 对轮廓进行多边形拟合
    for cnt in cnts:
        peri = cv2.arcLength(cnt, True) # 计算轮廓周长
        approx = cv2.approxPolyDP(cnt, # 轮廓
                                  0.02 * peri, # 精度
                                  True)
        if len(approx) == 4: # 四边形
            docCnt = approx
            break

print(docCnt)

# 用圆圈标记角点
points = []
for peak in docCnt:
    peak = peak[0]
    cv2.circle(im, tuple(peak), 10, (0, 0, 255), 2)
    points.append(peak)

cv2.imshow('im_circle', im)

# 校正
src = np.float32([points[0], points[1], points[2], points[3]])  # 原来逆时针方向四个点
dst = np.float32([[0, 0], [0, 488], [337, 488], [337, 0]])  # 对应变换后逆时针方向四个点
m = cv2.getPerspectiveTransform(src, dst)  # 生成透视变换矩阵
result = cv2.warpPerspective(im_gray.copy(), m, (337, 488))  # 透视变换
cv2.imshow("result", result)  # 显示透视变换结果

cv2.waitKey()
cv2.destroyAllWindows()