"""
    创建函数，在终端中录入int类型成绩。如果格式不正确，重新输入
"""
def get_score():
    while True:
        try:
            score = int(input("请输入成绩:"))
            if score < 0:
                print("输入成绩错误")
                continue
            return "成绩是: %d"%score
        except ValueError:
            print("输入成绩错误")


print(get_score())