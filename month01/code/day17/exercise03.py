from common.iterable_tools import IterableHelper

list01 = list(range(50))


def condition01(item):
    return item % 2


def condition02(item):
    # return item % 10 == 4 or item % 10 == 5
    return item % 10 in (4, 5)


for item in IterableHelper.find_all(list01, condition01):
    print(item)

for item in IterableHelper.find_all(list01, condition02):
    print(item)
