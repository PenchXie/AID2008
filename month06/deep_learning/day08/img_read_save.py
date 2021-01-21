"""
图像读取, 显示, 保存示例
"""
import cv2

# 读取图像
im = cv2.imread('../data/Linus.png',  # 图像路径
                1)  # 读取方式, 1-彩色, 0-灰度图像
print(type(im))  # 打印图像数据类型
print(im.shape)  # 打印图像形状

cv2.imshow('img_show',  # 窗口名称(重复覆盖)
           im)  # 图像数据
cv2.imwrite('Linus_new.png', im) # 保存图像

cv2.waitKey() # 等待用户敲击按键
cv2.destroyAllWindows() # 销毁所有创建的窗体
