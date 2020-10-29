"""
    字典练习
"""
# 创建
hong_kong = {
    'region': '香港',
    'new': 15,
    'existing': 393,
    'total': 4801,
    'cure': 4320,
    'death': 88,
}
shanghai = {
    'region': '上海',
    'new': 6,
    'existing': 61,
    'total': 903,
    'cure': 835,
    'death': 7,
}
xinjiang = {
    'region': '新疆',
    'new': 0,
    'existing': 49,
    'total': 902,
    'cure': 850,
    'death': 3,
}
# # 打印
# print(hong_kong)
# print(hong_kong['existing'])
# print(shanghai['existing'])
# print(shanghai['new'])
#
# print(xinjiang['new'])
# xinjiang['new'] += 1
# print(xinjiang['new'])
# 删除
# del hong_kong['existing']
# del xinjiang['new']
# del shanghai['new'], shanghai['existing']

# 遍历
# for key in hong_kong:
#     print(key)
[print(key) for key in hong_kong]

[print(value) for value in shanghai.values()]
#
# for key, value in xinjiang.items():
#     print(key)
#     print(value)
#
[print(key, value) for key, value in xinjiang.items()]
#
for key, value in shanghai.items():
    if value == 61:
        print(key)

[print(key) for key, value in shanghai.items() if value == 61]