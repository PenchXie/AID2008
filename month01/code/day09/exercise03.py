"""
    定义数值累乘的函数
"""


def accumulate_multiply(*args):
    result = 1
    for num in args:
        result *= num

    return result
