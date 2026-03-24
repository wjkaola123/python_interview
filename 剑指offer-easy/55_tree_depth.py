# Definition for a binary tree node.
import math


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.max_depth = 0
        self.elements = []

    def middle_order_transval(self, root):
        """
        中序二叉树遍历
        :param root:
        :return:
        """
        if not root:
            return

        self.elements.append(root.val)
        if root.left:
            self.middle_order_transval(root.left)
        if root.right:
            self.middle_order_transval(root.right)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    print(2 ** 1 - 1)
    print(2 ** 2 - 1)
    print(2 ** 3 - 1)
    print(2 ** 4 - 1)

    print(math.sqrt(3))
