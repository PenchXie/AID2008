class Commodity():
    def __init__(self, cid=0, name='', price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def print_info(self):
        print("商品编号%d,商品名称%s,商品单价%d" % (self.cid, self.name, self.price))


class Order():
    def __init__(self, cid=0, count=0):
        self.cid = cid
        self.count = count


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30)
]

list_orders = [
    Order(1001, 1),
    Order(1002, 3),
    Order(1005, 2)
]


def descend_order_by_price():
    for i in range(len(list_commodity_infos) - 1):
        for j in range(i + 1, len(list_commodity_infos)):
            if list_commodity_infos[i].price < list_commodity_infos[j].price:
                list_commodity_infos[i], list_commodity_infos[j] = list_commodity_infos[j], list_commodity_infos[i]


# 打印所有商品信息
def print_all_commidity_info():
    for commodity in list_commodity_infos:
        commodity.print_info()


# 打印商品单价小于2万的商品信息
def print_price_lt2000_commodity_info():
    for commodity in list_commodity_infos:
        if commodity.price < 20000:
            commodity.print_info()


# 打印所有订单中的商品信息
def print_order_commodity_info():
    for order in list_orders:
        for commodity in list_commodity_infos:
            if order.cid == commodity.cid:
                print(f"商品名称{commodity.name},商品单价:{commodity.price},数量{order.count}.")
                break


# 查找最贵的商品
def find_most_expensive():
    max_value = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if max_value.price < list_commodity_infos[i].price:
            # 使用更大的那个订单 替换 假设的订单
            max_value = list_commodity_infos[i]
    return max_value
