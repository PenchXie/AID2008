# 员工列表(员工编号 部门编号 姓名 工资)
dict_employees = {
    1001: {"did": 9002, "name": "师父", "money": 60000},
    1002: {"did": 9001, "name": "孙悟空", "money": 50000},
    1003: {"did": 9002, "name": "猪八戒", "money": 20000},
    1004: {"did": 9001, "name": "沙僧", "money": 30000},
    1005: {"did": 9001, "name": "小白龙", "money": 15000},
}

# 部门列表(部门编号,部门名称)
list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 9003, "title": "品保部"},
]
# 打印所有员工信息
for key in dict_employees:
    print(f"{dict_employees[key]['name']}员工编号是{key},部门编号是"
          f"{dict_employees[key]['did']},月薪{dict_employees[key]['money']}元")

# 打印所有月薪大于2w的员工信息
for key in dict_employees:
    if dict_employees[key]['money'] > 20000:
        print(f"{dict_employees[key]['name']}员工编号是{key},部门编号是"
              f"{dict_employees[key]['did']},月薪{dict_employees[key]['money']}元")

# 在部门列表中查找编号最小的部门
# didmin = list_departments[0]['did']
# did_num = 0
# # for i in range(len(list_departments)):
# for i in range(1, len(list_departments)):
#     if list_departments[i]['did'] < didmin:
#         didmin = list_departments[i]['did']
#         did_num = i
# print(list_departments[did_num])
min_item = list_departments[0]
for i in range(1, len(list_departments)):
    if min_item['did'] > list_departments[i]['did']:
        min_item = list_departments[i]
print(min_item)

# 根据部门编号对部门列表降序排列
for i in range(len(list_departments) - 1):
    for j in range(i + 1, len(list_departments)):
        if list_departments[i]['did'] < list_departments[j]['did']:
                list_departments[i], list_departments[j] = \
                list_departments[j], list_departments[i]
print(list_departments)