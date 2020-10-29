class CommodityController:
    def __init__(self):
        self.__commodity_list = []

    def add_commodity(self, name=''):
        self.__commodity_list.append(name)

    def __iter__(self):
        for commodity in self.__commodity_list:
            yield commodity


controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")

for item in controller:
    print(item)