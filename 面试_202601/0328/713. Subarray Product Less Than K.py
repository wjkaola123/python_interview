from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # l r
        # [l, r] [l+1, r] ... [r, r]
        # r -l + 1  固定r时, 得到满足条件的子数组的数量
        if k <= 1:
            return 0

        ans = left = 0
        prod = 1
        for right, n in enumerate(nums):
            prod *= n

            while prod >= k:
                prod /= nums[left]
                left += 1

            ans += right - left + 1

        return ans
