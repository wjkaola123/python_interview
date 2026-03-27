from math import inf
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0 # 左指针
        ans = inf # 设置一个超出数组长度的值
        s = 0
        # 双指针
        for right, num in enumerate(nums):
            s += num
            while s >= target:
                s -= nums[left]
                ans = min(ans, right - left + 1)
                left += 1

        return ans if ans <= n else 0