# 定义函数,删除商品字典中单价大于5000的所有商品信息
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}
# 定义函数,删除商品列表中单价大于5000的所有商品信息
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]


# def del_dict_price_gt5000():
#     del_list = []
#     for key, value in dict_commodity_infos.items():
#         if value['price'] > 5000:
#             del_list.append(key)
#     for key in del_list:
#         del dict_commodity_infos[key]


def del_dict_price_gt5000():
    key_list = list(dict_commodity_infos.keys())
    for key in key_list:
        if dict_commodity_infos[key]['price'] > 5000:
            del dict_commodity_infos[key]


def del_list_price_gt5000():
    for i in range(len(list_commodity_infos) - 1, -1, -1):
        if list_commodity_infos[i]['price'] > 5000:
            del list_commodity_infos[i]


# 字典推导式
dict_commodity_infos = {key: value for key, value in dict_commodity_infos.items() if value['price'] <= 5000}
# 列表推导式
list_commodity_infos = [item for item in list_commodity_infos if item['price'] <= 5000]

# del_dict_price_gt5000()
# del_list_price_gt5000()
print(dict_commodity_infos)
print(list_commodity_infos)
