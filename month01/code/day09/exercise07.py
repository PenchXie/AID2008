"""
    创建狗类
"""


class Dog():
    def __init__(self, breed, nickname, length, weight):
        self.breed = breed
        self.nickname = nickname
        self.length = length
        self.weight = weight

    def eat(self):
        self.weight += 1


Jack = Dog('中华田园犬', '狗狗', 90, 20)
print(Jack.__dict__)
Jack.eat()
print(Jack.__dict__)

John = Jack
Jack.weight = 30
print(John.weight)