from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)
