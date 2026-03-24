"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
and inorder is the inorder traversal of the same tree, construct and return the binary tree.
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        res = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        res.left = self.buildTree(preorder[1: idx + 1], inorder[0: idx])
        res.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])

        return res

