"""
    定义函数,根据总两数,计算几斤零几两
"""

def calc_jin_liang(total_liang):
    """
        计算重量
    :param total_liang: int类型, 总两数
    :return: tuple类型, (斤, 两)
    """
    jin = total_liang // 16
    liang = total_liang % 16
    return jin, liang

total_liang = int(input("请输入两:"))
tuple01 = calc_jin_liang(total_liang)
print(f"共{tuple01[0]}斤{tuple01[1]}两")