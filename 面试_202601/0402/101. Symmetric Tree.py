from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_mirror(p: Optional[TreeNode], q: Optional[TreeNode]):
            if p is None and q is None:
                return True

            if p is None or q is None:
                return False

            return p.val == q.val and is_mirror(p.left, q.right) and is_mirror(p.right, q.left)

        return is_mirror(root, root)
