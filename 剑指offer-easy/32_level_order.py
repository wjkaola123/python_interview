# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.first = True
        self.result = []

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return self.result
        if self.first:
            self.result.append([root.val])
            self.first = False

        if root.left and root.right:
            self.result.append([root.left.val, root.right.val])
        elif root.left and not root.right:
            self.result.append([root.left.val])
        elif not root.left and root.right:
            self.result.append([root.right.val])
        self.levelOrder(root.left)
        self.levelOrder(root.right)
        return self.result
