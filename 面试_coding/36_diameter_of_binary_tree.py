"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def calculate_depth(current: Optional[TreeNode]) -> int:
            # 如果是空节点, 直接返回 0
            if not current:
                return 0

            # 计算左右节点的深度
            l_depth = calculate_depth(current.left)
            r_depth = calculate_depth(current.right)

            nonlocal ans
            # 经过当前节点的路径长度 = 左子树深度 + 右子树深度
            # 我们用这个值来更新全局的最大直径
            ans = max(ans, l_depth + r_depth)

            return max(l_depth, r_depth) + 1

        calculate_depth(root)
        return ans