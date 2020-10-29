"""
    输入月份输出天数
"""
# 输入月份
month = input("请输入月份：")
#
# 判断并输出天数
if month in ['1', '3', '5', '7', '8', '10', '12']:
    print("31天")
elif month in ['4', '6', '9', '11']:
    print("30天")
elif month == '2':
    print("28天")
else:
    print("不正确的月份")

# # 另一种写法
# month = int(input("月份："))
#
# if month in range(1, 13):
#     if month == 2:
#         print("28")
#     elif month in [4, 6, 9, 11]:
#         print("30")
#     else:
#         print("31")
# else:
#     print("wrong month")