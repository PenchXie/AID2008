"""
    定义函数,根据年月日,计算星期
"""
import time


def calc_week_day(year, month, day):
    time_tuple = time.strptime("%s-%s-%s" % (year, month, day), "%Y-%m-%d")
    week_day_list = ('星期一', '星期二', '星期三', '星期四',
                     '星期五', '星期六', '星期日')
    return week_day_list[time_tuple[6]]

year = input("请输入年:")
month = input("请输入月:")
day = input("请输入日:")

print(calc_week_day(year, month, day))