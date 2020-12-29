import numpy as np

load_data = np.load('国民经济核算季度数据.npz', allow_pickle=True)
print(load_data.files)
print(load_data['columns'])
print(load_data['values'])