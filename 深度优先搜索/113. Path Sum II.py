# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        results = []
        res = []

        # 深度优先遍历函数
        # 第一步：优先考虑递归结束的条件，当前函数是找到了叶子节点，并且target_sum == root.val即为递归结束条件
        # 第二步: 递归结束时的操作, res.append, 并且存入到results, 再执行res.pop
        # 第三步：非结束条件对左子树的操作
        # 第四部：非结束条件对后子树的操作
        def dfs(root: TreeNode, target_sum: int):

            if not root:
                return
            if not root.left and not root.right:
                if target_sum == root.val:
                    res.append(root.val)
                    results.append(res[:])
                    res.pop()

            if root.left:
                res.append(root.val)
                target_sum -= root.val
                dfs(root.left, target_sum)
                target_sum += root.val
                res.pop()

            if root.right:
                res.append(root.val)
                target_sum -= root.val
                dfs(root.right, target_sum)
                target_sum += root.val
                res.pop()

        dfs(root, targetSum)
        return results


if __name__ == '__main__':
    pass
