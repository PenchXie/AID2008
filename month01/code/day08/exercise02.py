"""
    创建函数,根据课程阶段计算课程名称
"""


def find_course_name(step_num):
    course_dict = {
        '1': 'Python语言核心编程',
        '2': 'Python高级软件技术',
        '3': 'Web全栈',
        '4': '网络爬虫',
        '5': '数据分析、人工智能'
    }
    return course_dict[step_num]


step_num = input("请输入课程阶段数：")
print(find_course_name(step_num))
