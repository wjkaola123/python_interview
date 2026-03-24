from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination = []

        def dfs(target: int):
            if target == 0:
                sorted_combination = sorted(combination)
                if sorted_combination not in combinations:
                    combinations.append(sorted_combination)
            else:
                if target > 0:
                    for n in candidates:
                        combination.append(n)
                        dfs(target - n)
                        combination.pop()

        dfs(target)
        return combinations


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
