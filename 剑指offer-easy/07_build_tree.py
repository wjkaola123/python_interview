# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index = {val: i for i, val in enumerate(inorder)}

        def build(preRootId, inL, inR):
            if inL > inR:
                return None

            rootVal = preorder[preRootId]
            inRootId = index[rootVal]
            leftSize = inRootId - inL
            root = TreeNode(rootVal)
            root.left = build(preRootId + 1, inL, inRootId - 1)
            root.right = build(preRootId + 1 + leftSize, inRootId + 1, inR)

            return root

        return build(0, 0, len(inorder) - 1)
