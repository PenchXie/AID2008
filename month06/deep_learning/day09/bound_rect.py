"""
绘制矩形包围框
"""
import cv2
import numpy as np

im = cv2.imread('../data/cloud.png', 0)
cv2.imshow('im', im)

# 提取图像轮廓
ret, im_bin = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
img, cnt, hie = cv2.findContours(im_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print('contours[0].shape:', cnt[0].shape)

# 返回轮廓定点及边长
x, y, w, h = cv2.boundingRect(cnt[0])
print('x:', x, 'y:', y, 'w:', w, 'h:', h)

# 绘制矩形包围框
brcnt = np.array([[[x, y], [x + w, y], [x + w, y + h], [x, y + h]]])
cv2.drawContours(im, # 绘制图像
                 [brcnt],
                 -1, (255, 255, 255), 2)

cv2.imshow('result', im)

cv2.waitKey()
cv2.destroyAllWindows()