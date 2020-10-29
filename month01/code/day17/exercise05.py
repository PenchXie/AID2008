from common.iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money


# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

# def select_name():
#     for item in list_employees:
#         print(item.name)
#
# def select_id_money():
#     for item in list_employees:
#         print((item.eid, item.money))
#
# select_name()
# select_id_money()

[print(name) for name in IterableHelper.select(list_employees, lambda item: item.name)]
[print(item) for item in IterableHelper.select(list_employees, lambda item: (item.eid, item.money))]

print(IterableHelper.get_count(list_employees, lambda item: item.money > 20000))
print(IterableHelper.get_count(list_employees, lambda item: item.did == 9002))

# 删除
# IterableHelper.del_all(list_employees, lambda item: item.money > 30000)
# IterableHelper.del_all(list_employees, lambda item: item.did == 9001)
# for employee in list_employees:
#     print(employee.__dict__)

# 获取工资最高员工
print(IterableHelper.get_max(list_employees, lambda item: item.money).__dict__)

# 根据工资对员工列表进行升序排列
IterableHelper.ascending_order(list_employees, lambda item: item.money)
for emp in list_employees:
    print(emp.__dict__)