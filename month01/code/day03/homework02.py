"""
    根据年龄输出人生阶段
"""
# 获取年龄
age = int(input("请输入年龄："))

# 判断人生阶段
if age > 65:
    print("老年")
elif age > 40:
    print("中年")
elif age > 17:
    print("青年")
elif age > 6:
    print("少年")
elif age >= 0:
    print("童年")
else:
    print("非正常年龄")