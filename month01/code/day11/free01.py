class cls01():
    def __init__(self, arg):
        # 加__与不加__的区别：
        # 加__时, 在构造实例时会绕过set_arg函数, 即使数据不合理也能创建实例
        # 不加__时, 在构造实例时也会检测数据是否合理
        self.__arg = arg

    def get_arg(self):
        return self.__arg

    def set_arg(self, value):
        if value < 10:
            self.__arg = value
        else:
            raise Exception('ERROR')

    arg = property(get_arg, set_arg)
    # arg = property(None,set_arg)
    # arg = property(get_arg)

a = cls01(12)
print(a.__dict__)
a.arg = 12
print(a.__dict__)

# a.arg = 8
# print(a.__dict__)

# print(a.arg)