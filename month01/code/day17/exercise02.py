# 定义函数，在列表中查找奇数
# 定义函数，在列表中查找能被3或5整除的数字
list01 = list(range(10))


def find_number(func_condition):
    for item in list01:
        if func_condition(item):
            yield item


def condition01(item):
    return item % 2

def condition02(item):
    return item % 3 == 0 or item % 5 == 0

for item in find_number(condition01):
    print(item)

for item in find_number(condition02):
    print(item)