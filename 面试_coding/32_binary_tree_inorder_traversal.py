"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        in_order = []
        if not root:
            return in_order

        if root.left:
            left = self.inorderTraversal(root.left)
            in_order.extend(left)

        in_order.append(root.val)

        if root.right:
            right = self.inorderTraversal(root.right)
            in_order.extend(right)

        return in_order

class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def in_order(root):
            if not root:
                return

            if root.left:
                in_order(root.left)
            ans.append(root.val)
            if root.right:
                in_order(root.right)

        in_order(root)
        return ans