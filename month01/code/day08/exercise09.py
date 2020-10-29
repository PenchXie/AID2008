# 商品字典
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]


# 定义函数，打印所有商品信息
def print_commodity_info():
    for cid, c_dict in dict_commodity_infos.items():
        print_result(cid, c_dict)


# 定义函数，打印单价大于10000的商品信息
def print_price_gt_10000():
    for cid, c_dict in dict_commodity_infos.items():
        if c_dict['price'] > 10000:
            print_result(cid, c_dict)


def print_result(cid, c_dict):
    print(f"商品编号{cid},商品名称{c_dict['name']},商品单价{c_dict['price']}")


def find_order_max():
    max_value = list_orders[0]
    for i in range(1, len(list_orders)):
        if list_orders[i]['count'] > max_value['count']:
            max_value = list_orders[i]
    return max_value


def count_descend_order():
    for i in range(len(list_orders) - 1):
        for j in range(i + 1, len(list_orders)):
            if list_orders[i]['count'] < list_orders[j]['count']:
                list_orders[i], list_orders[j] = list_orders[j], list_orders[i]


print_commodity_info()
print_price_gt_10000()
max_value = find_order_max()
count_descend_order()
print(list_orders)
print(max_value)
