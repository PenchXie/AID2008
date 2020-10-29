"""
    继承练习
"""


class Car():
    def __init__(self, brand='', speed=120):
        self.brand = brand
        self.speed = speed


class ElectricCar(Car):
    def __init__(self, brand, speed, capacity, charge_power):
        super().__init__(brand, speed)
        self.capacity = capacity
        self.charge_power = charge_power


tesla = ElectricCar('Tesla', 100, 80, 80)
print(tesla.brand)
print(tesla.speed)
print(tesla.capacity)
print(tesla.charge_power)