"""
    创建图形管理器
"""
from typing import List


class ShapeManager():
    def __init__(self):
        self.__shapes_list = []  # type: List[Shape]

    def add_shape(self, shape):
        if isinstance(shape, Shape):
            self.__shapes_list.append(shape)

    def print_shape_area(self, shape):
        if shape in self.__shapes_list:
            return shape.calc_shape_area()

    def calc_total_area(self):
        total_area = 0
        for shape in self.__shapes_list:
            total_area += shape.calc_shape_area()

        return total_area

class Shape():
    def __init__(self):
        self.area = 0  # type: float

    def calc_shape_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius: float = 0):
        super().__init__()
        self.radius = radius

    def calc_shape_area(self):
        self.area = self.radius ** 2 * 3.14
        return self.area

    def __eq__(self, other):
        return self.radius == other.radius

class Rectangle(Shape):
    def __init__(self, length: float = 0, width: float = 0):
        super().__init__()
        self.length = length
        self.width = width

    def calc_shape_area(self):
        self.area = self.length * self.width
        return self.area

    def __eq__(self, other):
        return self.width == other.width and self.length == other.length


shapemanager01 = ShapeManager()
shapemanager01.add_shape(Circle(5.3))
shapemanager01.add_shape(Rectangle(3.2, 8.9))
print(shapemanager01.print_shape_area(Circle(5.3)))
# total_area = shapemanager01.calc_total_area()
# print(total_area)
# print(shapemanager01.calc_total_area())