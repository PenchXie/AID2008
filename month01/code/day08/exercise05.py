"""
    创建函数,根据年月计算天数
"""
def leap_year(year):
    return year % 4 == 0 and year % 100 or year % 400 == 0

def calc_day(year, month):
    """
    根据年份和月份输出月份天数
    :param year: int类型, 年份
    :param month: int类型, 月份
    :return: 输出天数或提示月份有误
    """
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    if month == 2:
        return 29 if leap_year(year) else 28
    return 0

print(calc_day(2100, 2))