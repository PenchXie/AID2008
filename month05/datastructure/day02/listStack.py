"""
python实现顺序栈模型
"""


class ListStack:
    def __init__(self):
        """初始化一个空栈"""
        self.elems = []

    def enstack(self, item):
        """入栈:相当于在列表尾部添加一个元素"""
        self.elems.append(item)

    def destack(self):
        """出栈:相当于列表的最后一个元素"""
        if not self.elems:
            raise Exception('destack from an empty stack')
        return self.elems.pop()

if __name__ == '__main__':
    s = ListStack()
    s.enstack(100)
    s.enstack(200)
    s.enstack(300)
    s.enstack(400)
    print(s.destack())
    print(s.destack())
    print(s.destack())
    print(s.destack())
    print(s.destack())