"""
    选择语句练习
"""
# 输入职位和年薪
position = input("Position:") == "高管"
salary = int(input("Yearly salary:")) > 500000

# 有一条件满足则打印娶你，否则打印继续努力
if position or salary:
    print("娶你")
else:
    print("继续努力")