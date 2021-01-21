"""
彩色图像直方图均衡化
"""
import cv2

im = cv2.imread('../data/sunrise.jpg')
cv2.imshow('im', im) # 显示原图

# BGR --> YUV(Y通道即为亮度通道)
im_yuv = cv2.cvtColor(
    im, # 原图
    cv2.COLOR_BGR2YUV)
# 取出亮度通道, 均衡化处理后覆盖原亮度通道
# ...表示前面两个维度取出所有的
im_yuv[..., 0] = cv2.equalizeHist(im_yuv[..., 0])
im_equ = cv2.cvtColor(im_yuv, cv2.COLOR_YUV2BGR) # YUV --> BGR

cv2.imshow('im_equ', im_equ)

cv2.waitKey()
cv2.destroyAllWindows()