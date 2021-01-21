"""
对单个通道进行操作
"""
import cv2

im = cv2.imread('../data/opencv2.png')
cv2.imshow('im', im)

# 取出蓝色通道
b = im[:, :, 0] # 0为蓝色分量
print(b.shape)
cv2.imshow('blue', b)

# 抹掉蓝色通道
im[:, :, 0] = 0 # 将所有蓝色信息删除
cv2.imshow('im-b0', im)

cv2.waitKey()
cv2.destroyAllWindows()