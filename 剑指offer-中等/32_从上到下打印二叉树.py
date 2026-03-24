# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        current_nodes = [root]
        next_nodes = []
        res.append([root.val])
        while current_nodes or next_nodes:
            for node in current_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)

            values = [node.val for node in next_nodes]
            if values:
                res.append(values)
            current_nodes = next_nodes
            next_nodes = []
        return res


if __name__ == '__main__':
    pass
