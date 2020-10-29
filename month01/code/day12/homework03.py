class Wife:
    def __init__(self, name="", height=0, face_score=0):
        self.name = name
        self.height = height
        self.face_score = face_score

    def __str__(self):
        return "%s的身高是%d,颜值是%d" % (self.name, self.height, self.face_score)

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.face_score > other.face_score


list_wife = [
    Wife("双儿", 170, 98),
    Wife("阿珂", 173, 100),
    Wife("苏荃", 160, 99),
    Wife("丽丽", 167, 90),
    Wife("芳芳", 168, 92),
    Wife("苏荃", 160, 99),
]

# 根据格式打印老婆对象:xx的身高是xx,颜值是xx
print(Wife("双儿", 170, 98))

# 判断阿珂是否在列表中
ak = Wife("阿珂", 173, 100)
print(ak in list_wife)

# 计算苏荃在列表中存在的个数
sq = Wife("苏荃", 160, 99)
print(list_wife.count(sq))

# 查找颜值最高的老婆对象
print(max(list_wife))

# 根据颜值对老婆列表进行升序排列
list_wife.sort()
for wife in list_wife:
    print(wife)
