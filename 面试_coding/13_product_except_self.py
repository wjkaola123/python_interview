"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from functools import reduce
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        current_nums = []
        results = [1 for _ in range(len(nums))]
        for index in range(len(results)):
            current_nums[:] = nums[0:index] + nums[index + 1:]
            for num in current_nums:
                results[index] *= num

        return results

# s = Solution()
# print(s.productExceptSelf(nums=[-1,1,0,-3,3]))


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        current_nums = []
        results = [0 for _ in range(len(nums))]
        for index in range(len(results)):
            current_nums[:] = nums[0:index] + nums[index + 1:]
            results[index] = reduce(lambda x, y: x * y, current_nums)

        return results

# s = Solution2()
# print(s.productExceptSelf(nums=[-1,1,0,-3,3]))

# 动态规划思想
class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]

        suf = [1] * n
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        return [p * s for p, s in zip(pre, suf)]

s = Solution3()
print(s.productExceptSelf(nums=[-1,1,0,-3,3]))