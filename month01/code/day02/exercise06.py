"""
    预算符练习, 将两数转化成X斤X两的格式
"""
# 输入总两数
liang = int(input("请输入总两数："))
# print("结果为：" + liang // 16 + "斤" + liang % 16 + "两")
print("结果为：%d斤%d两" % (liang // 16, liang % 16))
