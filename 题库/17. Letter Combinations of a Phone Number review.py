from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combination = []
        combinations = []
        slength = len(digits)
        if slength == 0:
            return []

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(index: int):
            if len(combination) == slength:
                combinations.append("".join(combination))
            else:
                num = digits[index]
                for letter in phoneMap[num]:
                    combination.append(letter)
                    dfs(index + 1)
                    combination.pop()

        dfs(0)
        return combinations


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))
