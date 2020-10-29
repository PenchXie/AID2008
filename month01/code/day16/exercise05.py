class MyRangeIterator():
    def __init__(self, end_num=0):
        self.end_num = end_num
        self.num = -1

    def __next__(self):
        if self.num >= self.end_num - 1:
            raise StopIteration()
        self.num += 1
        return self.num


class MyRange():
    def __init__(self, number=0):
        self.number = number

    def __iter__(self):
        return MyRangeIterator(self.number)

for number in MyRange(5):
    print(number)