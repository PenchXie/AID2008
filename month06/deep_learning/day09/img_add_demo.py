"""
图像相加示例
"""
import cv2

im_a = cv2.imread('../data/lena.jpg', 0)
im_b = cv2.imread('../data/lily_square.png', 0)

dst1 = cv2.add(im_a, im_b) # 直接相加, 图像会过白, 过亮
# 加权求和
dst2 = cv2.addWeighted(im_a, 0.6, im_b, 0.4, 0) # 最后一个参数为亮度调节量

cv2.imshow('im_a', im_a)
cv2.imshow('im_b', im_b)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()