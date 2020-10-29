"""
    获取制定范围内的所有质数
"""


def get_prime_num(low, high):
    result_list = list(range(low, high))
    for i in range(len(result_list) - 1, -1, -1):
        for num in range(2, result_list[i]):
            if result_list[i] % num == 0:
                del result_list[i]
                break

    return result_list


print(get_prime_num(2, 100))
