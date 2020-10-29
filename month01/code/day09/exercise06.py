"""
    创建手机类
"""


class MobilePhone():
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def call(self):
        print("Someone is calling you.")


my_phone = MobilePhone('华为', 5000, 'black')
my_phone.call()

phone_2 = MobilePhone('苹果', 10000, 'white')
phone_2.call()
