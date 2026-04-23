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

        current_level = [root]
        next_level = []
        ans = [root.val]
        while current_level:  # 广度优先搜索
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if next_level:
                res = [n.val for n in next_level]
                ans.append(res[-1])
            current_level = next_level
            next_level = []

        return ans
