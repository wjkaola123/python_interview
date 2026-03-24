# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionTest:

    def __init__(self):
        self.alist = []
        self.blist = []

    def preorder(self, root: TreeNode, res_list: List):
        if not root:
            return None
        res_list.append(root.val)
        if root.left:
            self.preorder(root.left, res_list)
        if root.right:
            self.preorder(root.right, res_list)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        self.preorder(A, self.alist)
        self.preorder(B, self.blist)

        if not self.alist or not self.blist:
            return False

        if self.blist[0] not in self.alist:
            return False

        start = self.alist.index(self.blist[0])
        sublist = self.alist[start: start + len(self.blist)]

        if sublist == self.blist:
            return True
        else:
            return False


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node4 = TreeNode(4)
    node4.left = node1
    node4.right = node2
    node5 = TreeNode(5)
    nodeA = TreeNode(3)
    nodeA.left = node4
    nodeA.right = node5

    nodeb1 = TreeNode(1)
    nodeB = TreeNode(4)
    nodeB.left = nodeb1
    assert s.isSubStructure(nodeA, nodeB) == True
