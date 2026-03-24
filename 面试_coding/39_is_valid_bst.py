"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    pre = -inf

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):  # 左
            return False
        if root.val <= self.pre:  # 中
            return False
        self.pre = root.val
        return self.isValidBST(root.right)  # 右


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')) -> bool:
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)


s = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(s.isValidBST(root))

s = Solution2()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(s.isValidBST(root))
