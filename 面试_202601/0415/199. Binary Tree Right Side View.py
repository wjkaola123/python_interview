from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = [root.val]
        cur_level = [root]
        next_level = []
        while cur_level:
            for n in cur_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)

            res = [node.val for node in next_level]
            if res:
                ans.append(res[-1])
            cur_level = next_level
            next_level = []

        return ans
