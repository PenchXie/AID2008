"""
    根据消费金额计算折扣
"""
# 输入账户类型与消费金额
account_type = input("请输入账户类型：")
charge = float(input("请输入消费金额："))

# 计算折扣
if account_type == "vip":
    print("85折" if charge <= 500 else "8折")
else:
    print("9折" if charge >= 800 else "原价")