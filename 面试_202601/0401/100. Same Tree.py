from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is not None:
            return False

        if p is not None and q is None:
            return False

        if p and q and p.val != q.val:
            return False

        if p is None and q is None:
            return True

        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)

        return l and r and p.val == q.val
