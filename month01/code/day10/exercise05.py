"""
    保护数据有效性
"""


class Enemy():
    def __init__(self, name='', atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp

    @property
    def atk(self):
        return self.__attack

    @atk.setter
    def atk(self, value):
        if value in range(0, 101):
            self.__attack = value
        else:
            raise Exception("攻击力错误")

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        # if value in range(0, 501):
        #     self.__hp = value
        # else:
        #     raise Exception("生命值错误")
        if value > 500:
            value = 500
        elif value < 0:
            value = 0
        self.__hp = value

enemy01 = Enemy('李小龙', 100, 900)
print(enemy01.atk)
print(enemy01.hp)
