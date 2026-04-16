from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        n = len(digits)
        path = [""] * n

        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return

            for letter in letters[int(digits[i])]:
                path[i] = letter
                dfs(i + 1)

        dfs(0)
        return ans


s = Solution()
assert s.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
