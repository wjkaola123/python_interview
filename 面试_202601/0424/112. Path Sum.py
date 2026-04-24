from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = 0
        is_exist = False

        def dfs(root):
            if not root:
                return
            nonlocal ans
            nonlocal is_exist
            ans += root.val
            if not root.left and not root.right and ans == targetSum:
                is_exist = True

            dfs(root.left)
            dfs(root.right)
            ans -= root.val

        dfs(root)
        return is_exist
