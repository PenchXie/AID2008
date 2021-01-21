"""
彩色图像转换为灰度图像
"""
import cv2

im = cv2.imread('../data/Linus.png', 1)
cv2.imshow('im', im) # 显示原图
# 转灰度图像
im_gray = cv2.cvtColor(im, # 原图
                       cv2.COLOR_BGR2GRAY) # 转换方式
cv2.imshow('im_gray', im_gray)

cv2.waitKey()
cv2.destroyAllWindows()