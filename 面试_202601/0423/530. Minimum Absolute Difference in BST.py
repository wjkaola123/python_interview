from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = inf
        pre = -inf

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            nonlocal ans
            nonlocal pre
            ans = min(ans, root.val - pre)
            pre = root.val
            dfs(root.right)

        dfs(root)
        return ans
