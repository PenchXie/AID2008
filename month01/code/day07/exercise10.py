"""
    创建计算治愈比例的函数
"""
def calc_cure_ratio(confirmed, cure):
    cure_ratio = cure / confirmed * 100
    print(f"治愈比例为{cure_ratio:.2f}%")


confirmed = int(input("请输入确诊人数:"))
cure = int(input("请输入治愈人数:"))
calc_cure_ratio(confirmed, cure)

# 定义函数,根据总两数,计算几斤零几两
def calc_jin_liang(total_liang):
    jin = total_liang // 16
    liang = total_liang % 16
    print(f"共{jin}斤{liang}两")

total_liang = int(input("请输入两:"))
calc_jin_liang(total_liang)