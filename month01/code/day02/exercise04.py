"""
    数据转换练习
"""
# 输入单价、数量与支付金额
price = float(input("请输入商品单价："))
number = int(input("请输入购买数量："))
payment = int(input("请输入支付金额："))
# 计算找零
change = payment - price * number
# 提示找零
print("应找回：%.2f"%(change))