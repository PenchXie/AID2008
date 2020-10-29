"""
    函数参数
        实参参数
            星号元组形参
"""


# 星号元组形参
# 作用: 将多个位置实参合并为一个元组
# 价值: 可以让位置实参数量无限
# 注意: 建议命名为args
def func01(*args):
    print(args)


func01()
func01(1)
func01(1, 2, 3)
func01(args=1)
