"""
    创建函数,计算IQ等级
"""


def calc_IQ(ma, ca):
    iq = ma / ca * 100
    if iq >= 140:
        return "天才"
    if iq >= 120:
        return "超常"
    if iq >= 110:
        return "聪慧"
    if iq >= 90:
        return "正常"
    if iq >= 80:
        return "迟钝"

    return "低能"


for i in range(1, 100):
    print(str(i) + calc_IQ(i * 2 - 30, i))
