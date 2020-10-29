"""
求100000以内质数之和，写成一个函数
         写一个装饰器求一个这个函数运行时间

         将100000分成4等份 分别使用4个进程求
         每一份的质数之和，四个进程同时执行
         记录时间

         将100000分成10等份 分别使用10个进程求
         每一份的质数之和，10个进程同时执行
         记录时间
"""
import time
from multiprocessing import Process


def get_prime_number(lo=1, hi=2):
    for number in range(lo, hi + 1):
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                break
        else:
            yield number


def calc_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time()
        print("用时:", finish_time - start_time)
        # print("============================")
        print(result)
        return result

    return wrapper


@calc_time
def get_sum_prime_numbers(lo=1, hi=2):
    total = 0
    for number in get_prime_number(lo, hi):
        total += number

    return total


if __name__ == '__main__':

    quarter_list = [Process(target=get_sum_prime_numbers, args=(25000 * i + 1, 25000 * (i + 1) + 1)) for i in range(4)]

    decile_list = [Process(target=get_sum_prime_numbers, args=(10000 * i + 1, 10000 * (i + 1) + 1)) for i in range(10)]

    print("直接算")
    get_sum_prime_numbers(1, 100000)

    # 四等分开始
    quarter_start_time = time.time()
    for p in quarter_list:
        p.start()

    # 十等分开始
    decile_start_time = time.time()
    for p in decile_list:
        p.start()

    # 四等分回收
    for p in quarter_list:
        p.join()
    quarter_finish_time = time.time()

    # 十等分回收
    for p in decile_list:
        p.join()
    decile_finish_time = time.time()

    print("=============================")
    print("四进程所用时间:", quarter_finish_time - quarter_start_time)
    print("十进程所用时间:", decile_finish_time - decile_start_time)