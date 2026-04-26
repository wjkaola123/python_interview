from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        prod = 1
        if k <= 1:
            return 0

        for right, x in enumerate(nums):
            prod *= nums[right]
            while prod >= k:
                prod = prod / nums[left]
                left += 1
            ans += right - left + 1

        return ans
