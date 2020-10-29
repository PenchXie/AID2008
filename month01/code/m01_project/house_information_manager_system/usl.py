from bll import HouseManagerController


class HouseManagerView():
    def __init__(self):
        self.__controller = HouseManagerController()
        self.__active = True

    def __display_menu(self):
        print("1.显示所有房源信息")
        print("2.显示总价最高房源信息")
        print("3.显示面积最小房源信息")
        print("4.根据总价升序房源信息")
        print("5.根据面积降序房源信息")
        print("6.查看所有两室一厅房源信息")
        print("7.查看所有大于6层房源信息")
        print("8.查看房源类型信息")
        print("9.删除房源类型信息")
        print("10.退出")

    def __get_number(self, msg):
        while True:
            try:
                num = int(input(msg))
                return num
            except ValueError:
                print("输入错误")

    def __select_menu(self):
        selection = self.__get_number("请输入选项:")
        if selection == 1:
            self.__show_all_house_info()
        elif selection == 2:
            self.__show_max_total_price_house_info()
        elif selection == 3:
            self.__show_min_area_house_info()
        elif selection == 4:
            self.__total_price_ascending_order_house_info()
        elif selection == 5:
            self.__area_descending_order_house_info()
        elif selection == 6:
            self.__show_2r1l_house_info()
        elif selection == 7:
            self.__show_floor_gt6_house_info()
        elif selection == 8:
            self.__show_all_house_type_info()
        elif selection == 9:
            self.__del_house_info()
        elif selection == 10:
            self.__active = False

    def __show_all_house_info(self):
        for item in self.__controller.list_houses:
            print(item)
        # for item in enumerate(self.__controller.list_houses):
            # print(item[1].__dict__)

    def main(self):
        while self.__active:
            self.__display_menu()
            self.__select_menu()

    def __show_max_total_price_house_info(self):
        target_house = self.__controller.get_max_total_price()
        print(target_house)

    def __show_min_area_house_info(self):
        target_house = self.__controller.get_min_area()
        print(target_house)

    def __total_price_ascending_order_house_info(self):
        sorted_list = self.__controller.get_total_price_ascending_order_house_list()
        for item in sorted_list:
            print(item)

    def __area_descending_order_house_info(self):
        sorted_list = self.__controller.get_area_descending_order_house_list()
        for item in sorted_list:
            print(item)

    def __show_2r1l_house_info(self):
        filtered_list = self.__controller.get_2r1l_house_list()
        for item in filtered_list:
            print(item)

    def __show_floor_gt6_house_info(self):
        filtered_list = self.__controller.get_floor_gt6_house_list()
        for item in filtered_list:
            print(item)

    def __show_all_house_type_info(self):
        for key, value in self.__controller.get_all_house_type_info().items():
            print("%s\t%d" % (key, value))

    def __del_house_info(self):
        del_ids = input("请输入需要删除的房源编号:").split(", ")
        count = self.__controller.del_house_info(del_ids)
        print("共删除%d个数据" % count)


# 测试
if __name__ == '__main__':
    view01 = HouseManagerView()
    view01.main()