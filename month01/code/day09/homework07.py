"""
    创建桌子类
        数据：品牌,材质,尺寸(长,宽,高)
    创建电脑类
        数据:型号,CPU型号,内存大小,硬盘大小
        行为：开机,关机
"""


class Table():
    def __init__(self, brand, material, length, width, height):
        self.brand = brand
        self.material = material
        self.size = (length, width, height)


class Computer():
    def __init__(self, typeid, cputype, ram, disc):
        self.typeid = typeid
        self.cputype = cputype
        self.ram = ram
        self.disc = disc

    def start(self):
        pass

    def shutdown(self):
        pass
