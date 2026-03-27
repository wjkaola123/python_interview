from math import inf
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0  # 左指针
        ans = inf  # 设置一个超出数组长度的值
        s = 0
        # 双指针
        for right, num in enumerate(nums):
            s += num
            while s >= target:
                s -= nums[left]
                ans = min(ans, right - left + 1)
                left += 1

        return ans if ans <= n else 0


# 暴力求解
class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = inf
        s = 0
        for i in range(n):
            s = nums[i]
            if s >= target:  # 当前数已经大于目标数, 更新 ans
                ans = min(ans, 1)
            for j in range(i + 1, n):
                s += nums[j]
                if s >= target:
                    ans = min(ans, j - i + 1)

        return ans if ans != inf else 0


nums = [2, 3, 1, 2, 4, 3]

s = Solution()
ret = s.minSubArrayLen(7, nums)
print(ret)
