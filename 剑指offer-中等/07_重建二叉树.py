# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.results = []

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        d = {val: index for index, val in enumerate(inorder)}

        def build(preRootId, inL, inR):
            if inL > inR:
                return None

            root = TreeNode(preorder[preRootId])
            inRootId = d.get(preorder[preRootId])
            leftSize = inRootId - inL
            root.left = build(preRootId + 1, inL, inRootId - 1)
            root.right = build(preRootId + 1 + leftSize, inRootId + 1, inR)

            return root

        return build(0, 0, len(inorder) - 1)

    def preorder(self, root: TreeNode) -> List[int]:

        if root:
            self.results.append(root.val)
            if root.left:
                self.preorder(root.left)
            if root.right:
                self.preorder(root.right)

        return self.results

    def inorder(self, root: TreeNode) -> List[int]:
        res = []

        def inner(root: TreeNode):
            if root:
                if root.left:
                    inner(root.left)
                res.append(root.val)
                if root.right:
                    inner(root.right)
        inner(root)
        return res


if __name__ == '__main__':
    s = Solution()
    root = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    # 递归对树进行先序遍历
    print(s.preorder(root))
    print(s.inorder(root))
