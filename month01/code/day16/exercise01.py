class Skill():
    def __init__(self, name='', ATK=0, manacost=0):
        self.name = name
        self.ATK = ATK
        self.manacost = manacost

    @property
    def ATK(self):
        return self.__ATK

    @ATK.setter
    def ATK(self, value):
        if value in range(101):
            self.__ATK = value
        else:
            raise Exception("ATK error", 1001, "if value in range(101)")

    @property
    def manacost(self):
        return self.__manacost

    @manacost.setter
    def manacost(self, value):
        if value in range(51):
            self.__manacost = value
        else:
            raise Exception("manacost error", 1002, "if value in range(51)")

skill01 = Skill()
skill01.name = input("Enter skill name:")
while True:
    try:
        skill01.ATK = int(input("Enter skill ATK:"))
        skill01.manacost = int(input("Enter skill manacost:"))
        break
    except Exception as e:
        print(e.args)

print(skill01.__dict__)