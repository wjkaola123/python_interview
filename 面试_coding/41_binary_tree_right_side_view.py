"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 广度优先搜索,获取每一层最后一个元素, 即为 right side view.
        # 利用双端队列先进先出, 实现广度优先遍历的逻辑
        res, queue = [], deque()
        if root:
            queue.append(root)
        while queue:
            level_count = len(queue)  # 每一层的节点数
            for index in range(level_count):
                node = queue.popleft()
                if index == level_count - 1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 深度优先搜索实现, 按照 根节点 -> 右子树 -> 左子树的顺序进行访问
        res = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(res):
                res.append(node.val)

            depth += 1
            dfs(node.right, depth)
            dfs(node.left, depth)

        dfs(root, 0)
        return res
