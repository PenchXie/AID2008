"""
    元组练习, 根据月日,计算是这一年的第几天
"""
# 每月天数元组
day_of_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# 输入月, 日
month = int(input("请输入月:"))
day = int(input("请输入日:"))
# 计算天数并输出
total_days = sum(day_of_month[:month - 1]) + day
print(total_days)