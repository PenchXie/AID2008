# 员工列表(员工编号 部门编号 姓名 工资)
dict_employees = {
    1001: {"did": 9002, "name": "师父", "money": 60000},
    1002: {"did": 9001, "name": "孙悟空", "money": 50000},
    1003: {"did": 9002, "name": "猪八戒", "money": 20000},
    1004: {"did": 9001, "name": "沙僧", "money": 30000},
    1005: {"did": 9001, "name": "小白龙", "money": 15000},
}

# 部门列表
list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 9003, "title": "品保部"},
]


# 打印信息
def print_info(eid, einfo):
    """
    输入字典的键值对打印员工信息
    :param eid: 键, 表示员工编号
    :param einfo: 值, 为储存员工部门, 姓名, 月薪的字典
    :return:
    """
    print("%d编号%s员工%d部门月薪%d" % (eid, einfo['name'], einfo['did'], einfo['money']))


# 创建函数,打印所有员工信息
def print_employee_info():
    """
    打印dict_empolyees中所有员工的信息
    :return:
    """
    for eid, einfo in dict_employees.items():
        print_info(eid, einfo)


# 创建函数,打印所有月薪大于2w的员工信息
def print_money_gt_2w_info():
    """
    打印dict_employee中所有月薪大于2w的员工信息
    :return:
    """
    for eid, einfo in dict_employees.items():
        if einfo['money'] > 20000:
            print_info(eid, einfo)


# 创建函数,在部门列表中查找编号最小的部门
def find_min_id():
    min_dept = list_departments[0]
    for i in range(1, len(list_departments)):
        if list_departments[i]['did'] < min_dept['did']:
            min_dept = list_departments[i]

    return min_dept


# 创建函数,根据部门编号对部门列表升序排列
def did_ascending_order():
    for i in range(len(list_departments) - 1):
        for j in range(i + 1, len(list_departments)):
            if list_departments[i]['did'] > list_departments[j]['did']:
                list_departments[i], list_departments[j] = list_departments[j], list_departments[i]


print_employee_info()
print_money_gt_2w_info()
print(find_min_id())
did_ascending_order()
print(list_departments)
