"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        path = [''] * n * 2
        ans = []

        # 目前填了 left 个左括号，right 个右括号
        def dfs(left, right):

            if right == n:  # 填完 2n 个括号
                ans.append("".join(path))
                return

            if left < n:  # 可以填左括号
                path[left + right] = '('
                dfs(left + 1, right)

            if left > right:  # 可以填右括号
                path[left + right] = ')'
                dfs(left, right + 1)

        dfs(0, 0)
        return ans


s = Solution()
print(s.generateParenthesis(3))
