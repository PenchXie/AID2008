"""
python实现链式栈模型
"""


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkStack():
    def __init__(self):
        """初始化一个空栈"""
        self.head = None

    def enstack(self, item):
        """入栈:添加链表头节点"""
        new_node = Node(item)
        new_node.next, self.head = self.head, new_node

    def destack(self):
        """出栈:删除链表头节点"""
        if not self.head:
            raise Exception('destack from empty stack')
        value = self.head.value
        self.head = self.head.next
        return value