"""
python实现单链表
设计:
    1.数学模型:单链表
    2.设计一组操作
        is_empty(): 判断是否为空链表
        add(item): 在链表头部添加一个节点
        append(item): 在链表尾部添加一个节点
        traverse(): 遍历整个链表
        remove(item): 移除某个节点
        insert(pos,item): 在指定索引位置添加节点
"""


class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


class SingleLinklist:
    def __init__(self):
        """初始化一个空链表"""
        self.head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.head == None

    def add(self, item):
        """在链表头部添加一个节点"""
        node = Node(item)
        self.head, node.next = node, self.head

    def append(self, item):
        """在链表尾部添加一个节点"""
        if not self.head:
            self.add(item)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(item)

    def traverse(self):
        cur = self.head
        if not cur:
            return None
        while cur.next:
            yield cur
            cur = cur.next
        yield cur

    def remove(self, item):
        cur = self.head
        if not cur:
            raise Exception('remove from empty linklist!')
        if cur.value == item:
            self.head = cur.next
            return
        while cur.next:
            if cur.next.value == item:
                cur.next = cur.next.next
                break
            cur = cur.next

    def insert(self, pos, item):
        """在指定索引位置添加节点"""
        pass

    def reverse(self):
        pre = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        self.head = pre

if __name__ == '__main__':

    sll01 = SingleLinklist()
    sll01.append(1)
    # sll01.append(2)
    # sll01.append(3)
    # sll01.append(4)
    print(sll01.is_empty())
    # sll01.remove(4)
    sll01.reverse()
    for num in sll01.traverse():
        print(num)
