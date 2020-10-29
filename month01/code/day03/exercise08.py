"""
    真值表达式＆条件表达式练习
"""
state = "奇数" if int(input("请输入一个整数：")) % 2 else "偶数"

print(state)

year = int(input("请输入一个年份："))

boolean = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# 不建议
# boolean = not year % 4 and year % 100 or not year % 400

# day = 29 if boolean else 28
# print(day)

# 甚至不需要day
print(29 if boolean else 28)
# print(29 if (year % 4 == 0 and year % 100 != 0)　or year % 400 == 0 else 28)