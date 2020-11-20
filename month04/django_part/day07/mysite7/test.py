class cls1():
    dict01 = {}
    def func01(self):
        cls1.dict01['a'] = 1
        print(self.dict01)

a = cls1()
a.func01()
print(a.dict01)