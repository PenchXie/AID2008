"""
    使用学生列表封装以下三个列表中数据
"""

list_student_name = ["悟空", "八戒", "白骨精"]
list_student_age = [28, 25, 36]
list_student_sex = ["男", "男", "女"]

student_info_list = [
    ["悟空", "八戒", "白骨精"],
    [28, 25, 36],
    ["男", "男", "女"]
]

# student_list = [list(item) for item in zip(list_student_name, list_student_age, list_student_sex)]
# print(student_list)

class Student():
    def __init__(self, name='', age=0, sex=''):
        self.name = name
        self.age = age
        self.sex = sex

student_class_list = [Student(*item) for item in zip(*student_info_list)]

print(student_class_list)