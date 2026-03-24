from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for index, n in enumerate(nums):
            if n <= 0:
                continue

            if index == 0 and n > 1:
                return 1

            if nums[index] - nums[index - 1] > 1:
                if nums[index - 1] + 1 > 0:
                    return nums[index - 1] + 1
                else:
                    if nums[index] > 1:
                        return 1

        return nums[-1] + 1 if nums[-1] + 1 > 0 else 1
