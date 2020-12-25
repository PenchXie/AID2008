"""
python实现链式队列
"""
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkQueue():
    def __init__(self):
        self.head = None

    def enqueue(self, item):

        new_node = Node(item)
        new_node.next, self.head = self.head, new_node

    def dequeue(self):
        pass

if __name__ == '__main__':
    q = LinkQueue()
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
