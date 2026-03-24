from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        combination = []

        def backtrack(nums: List[int]) -> List[List[int]]:
            if not nums and combination not in combinations:
                combinations.append(combination[:])
            else:
                for index, n in enumerate(nums):
                    combination.append(n)
                    backtrack(nums[:index] + nums[index + 1:])
                    combination.pop()

        backtrack(nums)
        return combinations


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
