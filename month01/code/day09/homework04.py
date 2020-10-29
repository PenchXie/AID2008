list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]

# 定义函数,打印所有商品信息
for commodity in list_commodity_infos:
    print("商品编号%d,商品名称%s,商品单价%d" % (commodity['cid'], commodity['name'], commodity['price']))

# 定义函数,打印商品单价小于2万的商品信息
for commodity in list_commodity_infos:
    if commodity['price'] < 20000:
        print("商品编号%d,商品名称%s,商品单价%d" % (commodity['cid'], commodity['name'], commodity['price']))

# 定义函数,打印所有订单中的商品信息
for order in list_orders:
    for commodity in list_commodity_infos:
        if order['cid'] == commodity['cid']:
            print("商品名称%s,商品单价:%d,数量%d" % (commodity['name'], commodity['price'], order['count']))
            break # 跳出内部循环
