"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_same_tree(root.left, root.right)

    def is_same_tree(self, p, q):
        if p is None or q is None:
            return p is q

        return p.val == q.val and self.is_same_tree(p.left, q.right) and self.is_same_tree(p.right, q.left)
