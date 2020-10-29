"""
    运算符练习
"""
# 输入确诊人数与治愈人数
patient_number = int(input("请输入确诊人数："))
cure_number = int(input("请输入治愈人数："))
# 计算治愈率
cure_rate = cure_number / patient_number * 100

# 输出治愈比例
print("治愈比例为%.2f%%" % (cure_rate))
