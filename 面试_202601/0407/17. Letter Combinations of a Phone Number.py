from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mappings = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)
        path = [''] * n
        ans = []

        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return

            for c in mappings[int(digits[i])]:
                path[i] = c
                dfs(i + 1)

        dfs(0)
        return ans


s = Solution()
assert s.letterCombinations("23") == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
