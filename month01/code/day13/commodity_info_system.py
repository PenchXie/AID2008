from typing import List


class CommodityModel():
    def __init__(self, name='', price=0, cid=0):
        self.name = name
        self.price = price
        self.cid = cid


class CommodityInfoSystemView():
    def __init__(self):
        self.__active = True

    def __selections(self):
        print("1.添加商品")
        print("2.显示商品")
        print("3.删除商品")
        print("4.修改商品")
        print("5.退出")

    def __input_selection(self, controller):
        self.selection = input("请输入选项:")
        if self.selection == "1":
            self.__input_commodity_info(controller)
        elif self.selection == "2":
            self.__show_commodity_info(controller)
        elif self.selection == "3":
            self.__del_commodity_info(controller)
        elif self.selection == "4":
            self.__modify_commodity_info(controller)
        elif self.selection == "5":
            self.__active = False

    def __input_commodity_info(self, controller):
        name = input("请输入商品名称:")
        price = int(input("请输入商品价格:"))
        new_commodity = CommodityModel(name, price)
        controller.add_commodity(new_commodity)

    def __show_commodity_info(self, controller):
        for commodity in controller.commodity_list:
            print("商品编号:%d, 商品名称:%s, 商品价格:%d" %
                  (commodity.cid, commodity.name, commodity.price))

    def main(self, controller):
        while self.__active:
            self.__selections()
            self.__input_selection(controller)

    def __del_commodity_info(self, controller):
        cid = int(input("请输入要删除的商品编号:"))
        if controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_commodity_info(self, controller):
        cid = int(input("请输入要修改的商品编号:"))
        name = input("请输入商品的新名称:")
        price = int(input("请输入商品的新价格:"))
        commodity = CommodityModel(name, price, cid)
        if controller.modify_commodity(commodity):
            print("修改成功")
        else:
            print("修改失败")


class CommodityInfoSystemController():
    def __init__(self):
        self.__commodity_list = []  # type: List[CommodityModel]
        self.cid = 1000

    @property
    def commodity_list(self):
        return self.__commodity_list

    def add_commodity(self, commodity):
        if isinstance(commodity, CommodityModel):
            commodity.cid = self.cid
            self.cid += 1
            self.__commodity_list.append(commodity)

    def remove_commodity(self, cid):
        for i in range(len(self.__commodity_list)):
            if self.__commodity_list[i].cid == cid:
                del self.__commodity_list[i]
                return True
        return False

    def modify_commodity(self, commodity):
        for item in self.__commodity_list:
            if item.cid == commodity.cid:
                # item.__dict__ = commodity.__dict__
                item.name = commodity.name
                item.price = commodity.price
                return True
        return False


controller01 = CommodityInfoSystemController()
view01 = CommodityInfoSystemView()
view01.main(controller01)
