"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)
        if n == 0:
            return []

        path = [''] * n
        ans = []

        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return

            for c in letters[int(digits[i])]:
                path[i] = c
                dfs(i + 1)

        dfs(0)
        return ans


s = Solution()
print(s.letterCombinations("23"))
