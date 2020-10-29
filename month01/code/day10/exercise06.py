"""
    创建技能类，并保护数据在有效范围内
"""
class Skill():
    def __init__(self, name='', cd=0, damage=0, mana_cost=100):
        self.name = name
        self.cd = cd
        self.damage = damage
        self.mana_cost = mana_cost

    def get_cd(self):
        return self.__cd

    def set_cd(self, value):
        if value in range(0, 121):
            self.__cd = value
        else:
            raise Exception("冷却时间错误")

    cd = property(get_cd)

    cd = cd.setter(set_cd)

# skill01 = Skill('as', 67)
# print(skill01.cd)