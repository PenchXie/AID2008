class CommodityModel():
    def __init__(self, name='', price=0, cid=0):
        self.name = name
        self.price = price
        self.cid = cid


class CommodityInfoSystemView():
    def __init__(self):
        self.__active = True

    def __selections(self, controller):
        print("1.添加商品")
        print("2.显示商品")
        print("3.退出")
        self.selection = input("请输入选项:")
        self.__act(controller)

    def __act(self, controller):
        if self.selection == "1":
            name = input("请输入商品名称:")
            price = int(input("请输入商品价格:"))
            new_commodity = CommodityModel(name, price)
            controller.add_commodity(new_commodity)
        elif self.selection == "2":
            controller.show_commodity_info()
        elif self.selection == "3":
            self.__active = False

    def main(self, controller):
        while self.__active:
            self.__selections(controller)


class CommodityInfoSystemController():
    def __init__(self):
        self.__commodity_list = []
        self.cid = 1000

    def add_commodity(self, commodity):
        if isinstance(commodity, CommodityModel):
            commodity.cid = self.cid
            self.cid += 1
            self.__commodity_list.append(commodity)

    def show_commodity_info(self):
        for commodity in self.__commodity_list:
            print("商品编号:%d, 商品名称:%s, 商品价格:%d" %
                  (commodity.cid, commodity.name, commodity.price))


controller01 = CommodityInfoSystemController()
view01 = CommodityInfoSystemView()
view01.main(controller01)
