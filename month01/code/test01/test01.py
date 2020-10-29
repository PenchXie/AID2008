"""
    根据长度获取斐波那契数列
"""


def get_fibonacci(length):
    low = 1
    high = 1
    fibocacci = [1]

    for i in range(length - 1):
        fibocacci.append(high)
        high += low
        low = high - low

    return fibocacci


print(get_fibonacci(7))
