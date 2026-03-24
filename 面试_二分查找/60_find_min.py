from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        ans = float('inf')  # 正无穷
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid]:  # 左边有序
                ans = min(nums[l], ans)
                l = mid + 1
            else:  # 右边有序
                ans = min(nums[mid], ans)
                r = mid - 1

        return ans
