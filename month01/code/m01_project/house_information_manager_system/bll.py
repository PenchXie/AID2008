"""
    业务逻辑层
"""
from common.iterable_tools import IterableHelper
from dal import HouseDao


class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()

    @property
    def list_houses(self):
        return self.__list_houses

    def get_max_total_price(self):
        return max(self.__list_houses, key=lambda item: item.total_price)

    def get_min_area(self):
        return min(self.__list_houses, key=lambda item: item.area)

    def get_total_price_ascending_order_house_list(self):
        return sorted(self.__list_houses, key=lambda item: item.total_price)

    def get_area_descending_order_house_list(self):
        return sorted(self.__list_houses, key=lambda item: item.area, reverse=True)

    def get_2r1l_house_list(self):
        return filter(lambda item: item.house_type == '2室1厅', self.__list_houses)

    def get_floor_gt6_house_list(self):
        return filter(lambda item: int(item.floor[item.floor.index("共") + 1:item.floor.index(")") - 1]) > 6,
                      self.__list_houses)
        # return filter(get_floor_gt6, self.__list_houses)

    def get_all_house_type_info(self):
        result_dict = {}
        for item in self.__list_houses:
            if item.house_type in result_dict.keys():
                result_dict[item.house_type] += 1
            else:
                result_dict[item.house_type] = 1

        return result_dict

    def del_house_info(self, del_ids):
        return IterableHelper.del_all(self.__list_houses, lambda item: str(item.id) in del_ids)


# def get_floor_gt6(item):
#     begin = item.floor.index("共")
#     end = item.floor.index("层")
#     floor = int(item.floor[begin + 1:end])
#     return floor > 6

# 测试代码
if __name__ == '__main__':

    controller01 = HouseManagerController()
    # result_list_02 = controller01.get_2r1l_house_list()
    for item in controller01.get_floor_gt6_house_list():
        print(item)
