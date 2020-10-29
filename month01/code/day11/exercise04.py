"""
    父类与子类
"""


class Animal():
    def eat(self):
        print("eat")


class Dog(Animal):
    def run(self):
        print("run")


class Bird(Animal):
    def fly(self):
        print("fly")


Bob = Dog()
Holly = Bird()
animal01 = Animal()
animal01.eat()
Bob.eat()
Bob.run()
Holly.eat()
Holly.fly()

print(isinstance(Bob, Animal))
print(isinstance(animal01, Animal))
print(isinstance(Holly, Bird))
print(isinstance(animal01, Bird))
print()
print(issubclass(Dog, Animal))
print(issubclass(Animal, Animal))
print(issubclass(Bird, Animal))
print(issubclass(Animal, Dog))
print()
print(type(Bob) == Dog)
print(type(Bob) == Animal)
print(type(animal01) == Animal)
print(type(animal01) == Dog)
