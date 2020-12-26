class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def append(self, item):
        q = [self.root]
        node = Node(item)
        # 空树的情况
        if not self.root:
            self.root = node
            return
        while True:
            cur = q.pop(0)
            # 判断左孩子
            if cur.left:
                q.append(cur.left)
            else:
                cur.left = node
                return
            if cur.right:
                q.append(cur.right)
            else:
                cur.right = node
                return

    def breadth_traverse(self):
        q = [self.root]
        if not self.root:
            raise Exception('traverse empty tree')
        while q:
            cur = q.pop(0)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            yield cur

    def preorder_traverse(self, node):
        if not node:
            return
        print(node.value, end=' ')
        self.preorder_traverse(node.left)
        self.preorder_traverse(node.right)

    def inorder_traverse(self, node):
        if not node:
            return
        self.inorder_traverse(node.left)
        print(node.value, end=' ')
        self.inorder_traverse(node.right)

    def postorder_traverse(self, node):
        if not node:
            return
        self.postorder_traverse(node.left)
        self.postorder_traverse(node.right)
        print(node.value, end=' ')

if __name__ == '__main__':
    bt1 = BinaryTree()
    bt1.append(1)
    bt1.append(2)
    bt1.append(3)
    bt1.append(4)
    bt1.append(5)
    bt1.append(6)
    bt1.append(7)
    bt1.append(8)
    bt1.append(9)
    bt1.append(10)
    for node in bt1.breadth_traverse():
        print(node.value, end=' ')

    print()
    bt1.preorder_traverse(bt1.root)
    print()
    bt1.inorder_traverse(bt1.root)
    print()
    bt1.postorder_traverse(bt1.root)
