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

    def preorder_traverse(self):
        pass

    def inorder_traverse(self):
        pass

    def postorder_traverse(self):
        pass

if __name__ == '__main__':
    bt1 = BinaryTree()
    # bt1.append(1)
    # bt1.append(2)
    # bt1.append(3)
    # bt1.append(4)
    for node in bt1.breadth_traverse():
        print(node.value)

# 2 8 9 9 4 3 13 21 18 10