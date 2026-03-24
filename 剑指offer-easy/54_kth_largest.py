# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.nodes = []

    def preOrderTransval(self, root):
        if not root:
            return
        if root.left:
            self.preOrderTransval(root.left)
        self.nodes.append(root.val)
        if root.right:
            self.preOrderTransval(root.right)

    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        self.preOrderTransval(root)
        if self.nodes:
            self.nodes = sorted(self.nodes, reverse=True)
        return self.nodes[k - 1]


if __name__ == '__main__':
    s = sorted([5, 3, 6, 2, 4, 1], reverse=True)
    print(s[2])
