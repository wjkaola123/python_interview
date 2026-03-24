"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # 利用双端队列先进先出, 实现广度优先遍历的逻辑
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            # 存储同一层中的节点值
            tmp = []
            for _ in range(len(queue)):
                # 从队列头部取出节点并访问
                node = queue.popleft()
                tmp.append(node.val)
                # 将下一层的节点放入队列尾部
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res
