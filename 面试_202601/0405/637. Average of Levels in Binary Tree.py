from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        current_level = [root]
        next_level = []
        ans = [float(root.val)]
        while current_level:
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if not next_level:
                break
            # 计算next_level节点平均值
            s = 0
            length = len(next_level)
            for n in next_level:
                s += n.val
            ans.append(float(s / length))

            current_level = next_level
            next_level = []

        return ans
