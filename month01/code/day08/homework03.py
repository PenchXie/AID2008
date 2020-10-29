"""
    参照下列代码,定义函数,计算社保缴纳费用
"""


def calc_social_insurance(salary_before_tax):
    """
    根据税前工资计算社保费用
    :param salary_before_tax:float型, 税前工资
    :return:float型, 社保缴纳费用
    """
    return salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12) + 3


salary_before_tax = float(input("请输入税前工资："))
print("个人需要缴纳社保费用：%.2f" % (calc_social_insurance(salary_before_tax)))
