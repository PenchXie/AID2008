"""
使用两个顺序栈实现队列
"""
class Solution:
    def __init__(self):
        # 两个栈
        self.stacka = []
        self.stackb = []

    def push(self, item):
        """入队"""
        self.stacka.append(item)

    def qpop(self):
        """出队"""
        # 先从stackb中出队
        if self.stackb:
            return self.stackb.pop()
        # 如果stackb为空,把stacka中元素添加到stackb中
        while self.stacka:
            self.stackb.append(self.stacka.pop())
        if self.stackb:
            return self.stackb.pop()
        else:
            raise Exception('pop from empty queue')

if __name__ == '__main__':
    s = Solution()
    s.push(100)
    s.push(200)
    print(s.qpop())
    s.push(300)
    print(s.qpop())
    s.push(400)
    print(s.qpop())
    print(s.qpop())