from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        left_size = inorder.index(preorder[0])
        l = self.buildTree(preorder[1: left_size + 1], inorder[:left_size + 1])
        r = self.buildTree(preorder[left_size + 1:], inorder[left_size + 1:])
        return TreeNode(preorder[0], l, r)


s = Solution()
root = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print(root)
