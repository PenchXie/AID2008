"""
仿射变换示例
仿射变换: 旋转, 平移
"""
import numpy as np
import cv2

def translate(img, x, y):
    h, w = img.shape[:2] # 获取图像高度, 宽度

    # 定义平移矩阵
    M = np.float32([[1, 0, x],
                    [0, 1, y]])
    # 执行仿射变换
    shifted = cv2.warpAffine(img, # 原图
                             M, # 变换矩阵
                             (w, h)) # 输出图像高, 宽
    return shifted

def rotate(img, angle, center=None, scale=1.0):
    """
    图像旋转变换
    @param img: 原始图像数据
    @param angle: 旋转角度
    @param center: 旋转中心
    @param scale: 缩放比例
    @return: 返回旋转后的图像
    """
    h, w = img.shape[:2]
    # 中心处理
    if center is None:
        center = (w / 2, h / 2)

    # 计算旋转矩阵
    M = cv2.getRotationMatrix2D(center, # 中心
                                angle, # 角度
                                scale) # 缩放比率
    rotated = cv2.warpAffine(img, # 原图
                             M, #　变换矩阵
                             (w, h)) # 输出图像宽度, 高度
    return rotated

if __name__ == '__main__':
    im = cv2.imread('../data/Linus.png')
    cv2.imshow('im', im)

    # 平移
    shifted = translate(im, 50, 40)
    cv2.imshow('shifted', shifted)

    # 旋转
    rotated = rotate(im, -45)
    cv2.imshow('rotated', rotated)

    cv2.waitKey()
    cv2.destroyAllWindows()