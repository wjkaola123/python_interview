"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Do not return anything, modify root in-place instead.
采用头插法构建链表，也就是从节点 6 开始，在 6 的前面插入 5，在 5 的前面插入 4，依此类推。
为此，要按照 6→5→4→3→2→1 的顺序访问节点。如何遍历这棵树，才能实现这个顺序？

按照右子树 - 左子树 - 根的顺序 DFS 这棵树。
DFS 的同时，记录当前链表的头节点为 head。一开始 head 是空节点。

具体来说：
如果当前节点为空，返回。
递归右子树。
递归左子树。
把 root.left 置为空。
头插法，把 root 插在 head 的前面，也就是 root.right=head。
现在 root 是链表的头节点，把 head 更新为 root。
"""
class Solution:
    head = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.flatten(root.right)
        self.flatten(root.left)

        root.left = None
        root.right = self.head
        self.head = root


"""
先序遍历版本
"""
class Solution2:

    def flatten(self, root: Optional[TreeNode]) -> None:
        l1 = []
        def pre_order(root):
            if not root:
                return
            l1.append(root)
            pre_order(root.left)
            pre_order(root.right)

        pre_order(root)
        for index, e in enumerate(l1):
            e.left = None
            if index + 1 < len(l1):
                e.right = l1[index + 1]

