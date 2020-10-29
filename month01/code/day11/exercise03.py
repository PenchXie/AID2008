"""
    以面向对象思想,描述下列情景.
    玩家攻击敌人,敌人受伤(头顶爆字).
    玩家攻击敌人,敌人受伤(根据玩家攻击力，减少敌人的血量).
"""


class Player():
    def __init__(self, name, HP=100, ATK=10, DEF=10):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF

    def attack(self, target):
        self.HP -= target.ATK - self.DEF
        print(f"{self.name}攻击了{monster01.race}")
        target.damage(self)


class Monster():
    def __init__(self, race='', HP=20, ATK=20, DEF=5):
        self.race = race
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF

    def damage(self, player):
        print(f"{self.race}的HP减少了{player.ATK - self.DEF}")


player01 = Player('路人A')
monster01 = Monster('slime')
player01.attack(monster01)
