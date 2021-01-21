"""
图像裁剪示例(通过数组切片完成)
"""
import numpy as np
import cv2

# 随机裁剪
def random_crop(im, w, h):
    # 产生裁剪起始位置
    start_x = np.random.randint(0, im.shape[1])
    start_y = np.random.randint(0, im.shape[1])
    new_img = im[start_x:start_y + h, start_x:start_x + w]
    return new_img

# 中心裁剪
def center_crop(im, w, h):
    # 产生裁剪起始位置
    start_x = im.shape[1] // 2 - w // 2 # 起始x
    start_y = im.shape[0] // 2 - h // 2 # 起始x
    new_img = im[start_y:start_y + h, start_x:start_x + w]
    return new_img

if __name__ == '__main__':
    im = cv2.imread('../data/banana_1.png', 1)
    # 随机裁剪
    new_img = random_crop(im, 200, 200)
    cv2.imshow('random_crop', new_img)

    # 中心裁剪
    new_img2 = center_crop(im, 200, 200)
    cv2.imshow('center_crop', new_img2)

    cv2.waitKey()
    cv2.destroyAllWindows()