class GraphicIteration():
    def __init__(self, data=None):
        self.data = data
        self.__index = -1

    def __next__(self):
        if self.__index > len(self.data) - 2:
            raise StopIteration
        self.__index += 1
        return self.data[self.__index]


class GraphicController:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        self.__graphics.append(graphic)

    def __iter__(self):
        return GraphicIteration(self.__graphics)


controller = GraphicController()
controller.add_graphic("圆形")
controller.add_graphic("矩形")
controller.add_graphic("三角形")

for item in controller:
    print(item)
