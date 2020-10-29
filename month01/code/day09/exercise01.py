"""
    定义函数,根据小时、分钟、秒,计算总秒数
"""


def calc_seconds(hour=0, minute=0, second=0):
    # return f"{3600 * hour + 60 * minute + second}秒"
    return "%d秒" % (3600 * hour + 60 * minute + second)


# 调用：提供小时、分钟、秒
print(calc_seconds(6, 53, 9))

# 调用：提供分钟、秒
print(calc_seconds(minute=7, second=30))

# 调用：提供小时、秒
print(calc_seconds(3, second=45))

# 调用：提供分钟
print(calc_seconds(minute=45))
