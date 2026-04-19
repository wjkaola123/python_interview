from math import inf
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        start = 0
        end = start + k - 1
        s = 0
        max_avg = -inf

        while end < n:
            for i in range(start, end + 1):
                s += nums[i]

            max_avg = max(max_avg, s / k)
            s = 0
            start += 1
            end += 1

        return max_avg


s = Solution()
print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(s.findMaxAverage([5], 1))
print(s.findMaxAverage([0, 1, 1, 3, 3], 4))
print(s.findMaxAverage([-1], 1))
