"""
    列表练习, 创建列表, 添加元素, 列表操作
"""
# 创建列表
regions = ['香港', '上海', '新疆']
new_addition = [15, 6, 0]
existing = [393, 61, 49]

# 添加元素
regions.append('四川')
new_addition.append(0)
existing.append(27)
regions.insert(0, '台湾')
new_addition.insert(0, 0)
existing.insert(0, 19)

# 打印香港疫情信息
print(f"{regions[0]}地区新增{new_addition[0]}人现存{existing[0]}人")
# 修改地区列表后两个元素
regions[-2:] = ['XJ', 'SC']
# 打印地区列表元素
for region in regions:
    print(region)
# 倒序打印新增列表元素
for item in new_addition[::-1]:
    print(item)

# 在地区列表中删除新疆
regions.remove('XJ')
# 在新增列表中删除第1个元素
del new_addition[0]
# 在现有列表中删除前2个元素
del existing[:2]
print(new_addition)
print(existing)