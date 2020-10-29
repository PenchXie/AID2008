"""
    多个人的多个爱好
"""
dict_hobbies = {
    "于谦": ["抽烟", "喝酒", "烫头"],
    "郭德纲": ["说", "学", "逗", "唱"],
}
# 打印于谦的所有爱好(一行一个)
for hobby in dict_hobbies["于谦"]:
    print(hobby)

# 计算郭德纲所有爱好数量
print(len(dict_hobbies["郭德纲"]))

# 打印所有人(一行一个)
for person in dict_hobbies:
    print(person)

# 打印所有爱好(一行一个)
for hobbies in dict_hobbies.values():
    for hobby in list(hobbies):
        print(hobby)