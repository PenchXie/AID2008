"""
输入一棵二叉搜索树,输出双向链表
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.li = []

    def tree_to_linklist(self, root):
        self.inorder_traverse(root)
        # 空树或只有树根的树
        if not self.li or len(self.li) == 1:
            return root
        # 处理头尾节点
        self.li[0].left = None
        self.li[-1].right = None
        # 处理中间节点
        for i in range(1, len(self.li) - 1):
            self.li[i].left = self.li[i - 1]
            self.li[i].right = self.li[i + 1]
        return self.li[0]

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
    print(s.tree_to_linklist(t12).value)