list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]

# 使用生成器表达式在列表中获取所有字符串
generator01 = (item for item in list01 if type(item) == str)
for string in generator01:
    print(string)

# 在列表中获取所有整数,并计算它的平方
generator02 = (item ** 2 for item in list01 if type(item) == int)
for num in generator02:
    print(num)