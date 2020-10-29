"""
    运算符练习, 计算加速度
"""
# 录入位移、时间、初速度
s = float(input("请输入位移："))
t = float(input("请输入时间："))
v_0 = float(input("请输入初速度："))

# 计算加速度
a = ( s - v_0 * t ) * 2 / t ** 2

# 输出加速度
print("加速度：" + str(a))