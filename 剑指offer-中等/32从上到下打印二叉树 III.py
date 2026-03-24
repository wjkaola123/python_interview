# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        current_nodes = [root]
        next_nodes = []
        res = [[root.val]]
        is_reverse = False
        while current_nodes or next_nodes:
            for node in current_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            temp_nodes = []
            for node in next_nodes:
                temp_nodes.append(node.val)

            if temp_nodes:
                is_reverse = not is_reverse
                if is_reverse:
                    temp_nodes.reverse()
                res.append(temp_nodes)
            current_nodes = next_nodes
            next_nodes = []

        return res
