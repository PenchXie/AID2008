"""
    类变量, 局部变量
"""


class MyClass():
    data02 = 20
    def __init__(self):
        self.data01 = 10
        self.data01 += 1
        MyClass.data02 += 1

m01 = MyClass()
m02 = MyClass()
m03 = MyClass()
print(m03.data01)
print(MyClass.data02)
print(m03.data02)
m03.data02 = 30
print(m03.data02)
print(MyClass.data02)
