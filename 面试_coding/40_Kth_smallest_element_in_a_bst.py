"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def preorder(node):
            # 对二叉树做中序遍历, 返回数组中第K个数字即可
            if node is None:
                return

            if node.left:
                preorder(node.left)
            res.append(node.val)

            if node.right:
                preorder(node.right)

        preorder(root)

        return res[k - 1]
