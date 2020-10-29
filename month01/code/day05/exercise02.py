"""
    列表练习
"""
# 创建行星列表
planets = ['水星', '金星', '火星', '木星']

# 插入"地球"、追加"土星" "天王星" "海王星"
planets.insert(2, '地球')
# planets.append('土星')
# planets.append('天王星')
# planets.append('海王星')
planets += ["土星", "天王星", "海王星"]

# 打印距离太阳最近、最远的行星(第一个和最后一个元素)
print(planets[0])
print(planets[-1])

# 打印太阳到地球之间的行星(前两个行星)
print(planets[:2])

# 删除"海王星",删除第四个行星
planets.remove('海王星')
del planets[3]

# 倒序打印所有行星(一行一个)
for planet in planets[::-1]:
    print(planet)

