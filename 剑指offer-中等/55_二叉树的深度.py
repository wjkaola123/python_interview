# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        max_depth = 0
        if not root:
            return max_depth
        current_nodes = [root]
        next_nodes = []
        while current_nodes or next_nodes:
            for node in current_nodes:
                if node and node.left:
                    next_nodes.append(node.left)
                if node and node.right:
                    next_nodes.append(node.right)
            current_nodes = next_nodes
            next_nodes = []
            max_depth += 1

        return max_depth


if __name__ == '__main__':
    node7 = TreeNode(7)
    node15 = TreeNode(15)
    node20 = TreeNode(20)
    node20.left = node15
    node20.right = node7
    node9 = TreeNode(9)
    root = TreeNode(3)
    root.left = node9
    root.right = node20

    s = Solution()
    print(s.maxDepth(root))
