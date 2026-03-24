# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        current = root
        tmp = current.left
        current.left = current.right
        current.right = tmp
        self.mirrorTree(current.left)
        self.mirrorTree(current.right)
        return root


if __name__ == '__main__':
    pass
