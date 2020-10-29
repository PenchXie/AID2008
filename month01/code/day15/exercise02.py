"""
    定义函数,根据生日(年月日),计算活了多天
"""
import time

def calc_live_days(year, month, day):
    local_time = time.mktime(time.localtime())
    birth_date_tuple = time.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
    birth_time = time.mktime(birth_date_tuple)
    return int((local_time - birth_time) / 3600 / 24)

print(calc_live_days(1949, 10, 1))