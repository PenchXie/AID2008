import numpy as np
import sklearn.preprocessing as sp

raw_sample = np.array([[65.5, 89.0, 73.0],
                       [55.0, 99.0, 98.5],
                       [45.0, 22.5, 60.0]])
bin_sample = raw_sample.copy()
# 生成掩码
mask1 = bin_sample < 60
mask2 = bin_sample >= 60
# print(mask1)
# print(mask2)

# 将mask1中为True的置为0
bin_sample[mask1] = 0
# 将mask2中为True的置为1
bin_sample[mask2] = 1
print(bin_sample)

print("================")
binary = sp.Binarizer(threshold=59) # 注意阈值
bin_sample = binary.fit_transform(raw_sample)
print(bin_sample)