# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def preorder_transval(self, root: TreeNode):
        preorder_nodes = []
        if not root:
            return None
        preorder_nodes.append(root.val)
        if root.left:
            preorder_nodes.extend(self.preorder_transval(root.left))
        if root.right:
            preorder_nodes.extend(self.preorder_transval(root.right))

        return preorder_nodes

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        preorder_a = self.preorder_transval(A)
        preorder_b = self.preorder_transval(B)

        if not preorder_a or not preorder_b:
            return False

        if preorder_a:
            a = ''.join([f'{item}' for item in preorder_a])
        if preorder_b:
            b = ''.join([f'{item}' for item in preorder_b])

        return True if b in a else False

    def isSubStructure2(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


if __name__ == '__main__':
    node11 = TreeNode(11)
    node3 = TreeNode(3)
    node3.left = node11
    node6 = TreeNode(6)
    node8 = TreeNode(8)
    node12 = TreeNode(12)
    node12.left = node6
    node12.right = node8
    nodeA = TreeNode(10)
    nodeA.left = node12
    nodeA.right = node3

    nodeB = TreeNode(10)
    node6 = TreeNode(6)
    node8 = TreeNode(8)
    node12 = TreeNode(12)
    node12.left = node6
    node12.right = node8
    nodeB.left = node12

    s = Solution()
    print(s.isSubStructure(nodeA, nodeB))
