"""
思路:
    1.利用队列思想:append() + pop(0)
    2.一个队列存储当前层,一个队列存储下一层,利用交换变量思想
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def print_binarytree_by_layer(self, root):
        # 当前层
        curq = [root]
        # 下一层
        nextq = []
        # 打印当前层,添加下一层
        while curq:
            node = curq.pop(0)
            print(node.value, end=' ')
            # 左右孩子添加到下一层
            if node.left:
                nextq.append(node.left)
            if node.right:
                nextq.append(node.right)
            # 打印完当前层后再交换两个列表
            if not curq:
                print()
                curq, nextq = nextq, curq

    def print_binary_tree_by_layer_reverse(self, root):
        # 当前层
        curq = [root]
        # 下一层
        nextq = []
        # 层数 
        i = 0

        while curq:
            node = curq.pop(0)
            index = 0 if (-1) ** i > 0 else -1
            print(node.value, end=' ')
            # 左右孩子添加到下一层
            binary_list = [node.left, node.right]
            while binary_list:
                next_node = binary_list.pop(index)
                if next_node:
                    nextq.append(next_node)

            if not curq:
                print()
                curq, nextq = nextq[::-1], curq
                i += 1

if __name__ == '__main__':
    s = Solution()
    p1 = Node(1)
    p2 = Node(2)
    p3 = Node(3)
    p4 = Node(4)
    p5 = Node(5)
    p6 = Node(6)
    p7 = Node(7)
    p8 = Node(8)
    p9 = Node(9)
    p10 = Node(10)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p6
    p3.right = p7
    p4.left = p8
    p4.right = p9
    p5.left = p10
    s.print_binarytree_by_layer(p1)
    s.print_binary_tree_by_layer_reverse(p1)