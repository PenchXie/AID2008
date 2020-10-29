# 定义函数,在列表中找出所有偶数
list01 = [43, 43, 54, 56, 76, 87, 98]


def find_even_number(target_list):
    for number in target_list:
        if number % 2 == 0:
            yield number


for number in find_even_number(list01):
    print(number)

# 定义函数,在列表中找出所有数字
list02 = [43, "悟空", True, 56, "八戒", 87.5, 98]


def find_number(target_list):
    for item in target_list:
        # if type(item) == int or type(item) == float:
        # 更好的写法
        if type(item) in (int, float):
            yield item


for number in find_number(list02):
    print(number)
