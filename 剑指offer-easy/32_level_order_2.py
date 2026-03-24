# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        current_nodes = [root]
        next_nodes = []
        res.append([item.val for item in current_nodes])
        while current_nodes or next_nodes:
            for node in current_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)

            if next_nodes:
                res.append([item.val for item in next_nodes])

            current_nodes = next_nodes
            next_nodes = []

        return res
