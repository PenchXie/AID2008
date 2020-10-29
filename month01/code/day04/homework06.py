"""
    模拟登录
"""
# 设置账号密码和登录次数
account = "admin"
pwd = "123456"
chances = 3

while True:
    # 提示输入账号密码
    enter_account = input("请输入账号：")
    enter_pwd = input("请输入密码：")

    # 账号或密码错误时提示, 并chances - 1
    if account != enter_account or pwd != enter_pwd:
        print("登录失败")
        chances -= 1
        if chances > 0:
            continue
        print("锁定账户")
        break
    else:
        print("登录成功")
        break
