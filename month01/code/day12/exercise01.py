class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}的编号是{self.cid},单价是{self.price}"

class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp

    def __str__(self):
        return f"{self.name}的攻击力是{self.atk},血量是{self.hp}"


cola = Commodity(1, '可乐', 3)
slime = Enemy('史莱姆', 20, 20)
print(cola)
print(slime)