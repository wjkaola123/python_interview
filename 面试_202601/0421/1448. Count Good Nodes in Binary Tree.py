from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root, path_max):
            if not root:
                return 0

            nonlocal ans  # 全局变量
            if root.val >= path_max:  # path_max 是从root节点到当前节点的路径最大值
                ans += 1  # 全局变量加1
                path_max = root.val  # 更新path_max

            dfs(root.left, path_max)  # 继续遍历左子树
            dfs(root.right, path_max)  # 继续遍历右子树

        dfs(root, -inf)  # 执行函数
        return ans
