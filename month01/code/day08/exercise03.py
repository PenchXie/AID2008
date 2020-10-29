"""
    创建函数,计算梯形面积
"""
def calc_trapezoid_area(top_base, bottom_base, height):
    return (top_base + bottom_base) * height / 2

print(calc_trapezoid_area(1, 2, 5))