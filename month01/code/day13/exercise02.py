class Character():
    def __init__(self, name: str = '', HP: int = 0, ATK: int = 0, DEF: int = 0):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF

    def attack(self, target):
        if isinstance(target, Character):
            if self.ATK >= target.DEF:
                target.HP -= self.ATK - target.DEF
                target.injure(self)

    def injure(self, attacker):
        if isinstance(attacker, Character):
            if self.DEF <= attacker.ATK:
                self.HP -= attacker.ATK - self.DEF


class Player(Character):
    def injure(self, attacker):
        super().injure(attacker)
        print("闪现红屏")


class Enemy(Character):
    def injure(self, attacker):
        super().injure(attacker)
        print("掉落装备")


xm = Player('小明', 1000, 10, 10)
slime = Enemy('史莱姆', 20, 20, 5)
xm.attack(slime)
slime.attack(xm)