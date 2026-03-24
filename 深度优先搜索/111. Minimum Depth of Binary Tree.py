# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        ldepth = self.minDepth(root.left)
        rdepth = self.minDepth(root.right)

        if not root.left or not root.right:
            return ldepth + rdepth + 1

        return min(ldepth, rdepth) + 1
