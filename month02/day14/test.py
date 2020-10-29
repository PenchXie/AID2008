class Person():
    def __init__(self, age):
        self.__age = self.setage(age)

    def setage(self, age):
        if age < 0:
            self.__age = 0
        else:
            self.__age = age

    def getage(self):
        return self.__age

p1 = Person(12)

# p1.setage(-5)

print(p1.getage())