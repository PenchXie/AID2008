"""
    使用闭包模拟以下情景
"""


# 在银行开户存入10000
def create_account(money):
    def buy(commodity, cost):
        nonlocal money
        money -= cost
        print(f"购买{commodity}花了{cost}元, 账户剩余{money}元")

    return buy


action = create_account(10000)
action('奥特曼', 100)
action('switch', 2000)
