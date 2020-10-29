"""
    以面向对象思想,描述下列情景.
    小明请保洁打扫卫生
"""


class Employer():
    def __init__(self, name='', employee=None):
        self.name = name
        self.employee = employee

    # def employ(self, employee):
    #     print(self.name, "请", employee.position, employee.work())

    # def employ(self):
    #     bj = Employee('保洁', '打扫卫生')
    #     print(self.name, "请", bj.position, bj.work())

    def employ(self):
        print(self.name, "请", self.employee.position, self.employee.work())


class Employee():
    def __init__(self, position='', description=''):
        self.position = position
        self.description = description

    def work(self):
        return self.description


xm = Employer('小明', employee01)
employee01 = Employee('保洁', '打扫卫生')
# xm.employ(employee01)
xm.employ()
