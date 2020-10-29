class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def __gt__(self, other):
        return self.money > other.money

    def __eq__(self, other):
        return self.eid == other.eid

list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

max_emp = max(list_employees)
print(max_emp.__dict__)
list_employees.sort()
for emp in list_employees:
    print(emp.__dict__)

target = Employee(1003, 9002, '猪八戒', 20000)
print(list_employees.index(target))