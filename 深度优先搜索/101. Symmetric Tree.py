# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def dfs(L, R) -> bool:
            if not L and not R:
                return True
            if not L or not R:
                return False
            if L.val != R.val:
                return False
            return dfs(L.left, R.right) and dfs(L.right, R.left)

        return dfs(root.left, root.right)
