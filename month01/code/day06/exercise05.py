"""
    字典推导式练习
"""
names = ["张无忌","赵敏","周芷若"]
rooms = [101,102,103]

# 将两个列表，合并为一个字典
dict01 = {rooms[i]: names[i] for i in range(3)}
print(dict01)
# print({rooms[i]: names[i] for i in range(3)})

# 颠倒键值对
# dict02 = {}
# for key in dict01:
#     dict02[dict01[key]] = key
# print(dict02)

dict02 = {value: key for key, value in dict01.items()}
print(dict02)

