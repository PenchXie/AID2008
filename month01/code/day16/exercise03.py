class CommodityIterator():
    def __init__(self, data=None):
        self.data = data
        self.__index = -1

    def __next__(self):
        if self.__index >= len(self.data) - 1:
            raise StopIteration
        self.__index += 1
        return self.data[self.__index]


class CommodityController:
    def __init__(self):
        self.__commodity_list = []

    def add_commodity(self, name=''):
        self.__commodity_list.append(name)

    def __iter__(self):
        return CommodityIterator(self.__commodity_list)


controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")

for item in controller:
    print(item)
