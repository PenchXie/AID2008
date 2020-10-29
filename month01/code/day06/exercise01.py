"""
    列表推导式
"""
# 生成10--30之间能被3或者5整除的数字
list01 = [num for num in range(10, 31) if num % 3 == 0 or num % 5 == 0]
print(list01)

# 生成5 -- 20之间的数字平方
list02 = [num ** 2 for num in range(5, 21)]
print(list02)