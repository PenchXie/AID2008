"""
    以面向对象的思想，描述以下情景:
    小明在银行取钱（银行钱少了，小明钱多了）
"""


class Person():
    def __init__(self, money=0):
        self.money = money

    def withdraw_money(self, bank, amount):
        self.money += amount
        bank.money -= amount


class Bank():
    def __init__(self, name='', money=10000):
        self.name = name
        self.money = money




xm = Person(1000)
boc = Bank('中国银行', 20000)
print(xm.money)
print(boc.money)

xm.withdraw_money(boc, 5000)
print(xm.money)
print(boc.money)
