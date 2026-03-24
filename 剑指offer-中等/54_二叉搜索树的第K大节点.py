# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        values = []

        def recur(node: TreeNode):
            if node:
                values.append(node.val)
            if node.left:
                recur(node.left)
            if node.right:
                recur(node.right)

        recur(root)
        values = sorted(values, reverse=True)
        print(values)
        return values[k - 1]


if __name__ == '__main__':
    node2 = TreeNode(2)
    node1 = TreeNode(1)
    node1.right = node2
    node4 = TreeNode(4)
    root = TreeNode(3)
    root.left = node1
    root.right = node4

    s = Solution()
    print(s.kthLargest(root, 2))
