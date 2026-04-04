from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        root_val = postorder[-1]
        root_index = inorder.index(root_val)
        left_inorder = inorder[: root_index]
        left_postorder = postorder[: len(left_inorder)]

        right_inorder = inorder[root_index + 1:]
        right_postorder = postorder[len(left_inorder): -1]
        left = self.buildTree(left_inorder, left_postorder)
        right = self.buildTree(right_inorder, right_postorder)

        return TreeNode(root_val, left, right)


def print_tree(root):
    if not root:
        return "null"
    return f"{root.val}({print_tree(root.left)},{print_tree(root.right)})"


s = Solution()
result = s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
print(print_tree(result))
