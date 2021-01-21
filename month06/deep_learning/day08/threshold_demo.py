"""
二值化处理示例
"""
import cv2

im = cv2.imread('../data/lena.jpg', 0)
cv2.imshow('im', im)

# 二值化
t, im_bin = cv2.threshold(
    im, # 原图
    127, # 阈值
    255, # 最大值
    cv2.THRESH_BINARY) # 选项: 二值化
cv2.imshow('im_bin', im_bin)

# 反二值化
t, im_bin2 = cv2.threshold(
    im, # 原图
    127, # 阈值
    255, # 最大值
    cv2.THRESH_BINARY_INV) # 选项: 二值化
cv2.imshow('im_bin2', im_bin2)

cv2.waitKey()
cv2.destroyAllWindows()