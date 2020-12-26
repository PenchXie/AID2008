"""
给定一棵二叉搜索树,找出其中第K小的节点
思路:
    1.特点:中序遍历的结果是递增的序列
    2.先中序遍历拿到递增的序列,再利用列表的索引值
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.li = []

    def get_k_node(self, root, k):
        # li = self.inorder_traverse(root)
        self.inorder_traverse(root)
        return self.li[k - 1]

    def inorder_traverse(self, root):
        if not root:
            return
        self.inorder_traverse(root.left)
        self.li.append(root)
        self.inorder_traverse(root.right)


if __name__ == '__main__':
    s = Solution()
    t12 = TreeNode(12)
    t5 = TreeNode(5)
    t18 = TreeNode(18)
    t2 = TreeNode(2)
    t9 = TreeNode(9)
    t15 = TreeNode(15)
    t19 = TreeNode(19)
    t17 = TreeNode(17)
    t16 = TreeNode(16)
    # 开始创建树
    t12.left = t5
    t12.right = t18
    t5.left = t2
    t5.right = t9
    t18.left = t15
    t18.right = t19
    t15.right = t17
    t17.left = t16
    print(s.get_k_node(t12, 11).value)
