"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 1:
            return

        head = nums[-k%length:]
        for n in nums[:-k%length]:
            head.append(n)

        nums[:] = head


# Test
nums = [1, 2, 3, 4, 5, 6, 7]
sol = Solution()
sol.rotate(nums, 3)
print(nums)

nums = [-1,-100,3,99]
sol.rotate(nums, 2)
print(nums)


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums[:] = nums[-k%length:] + nums[:-k%length]


nums = [-1,-100,3,99]
sol1 = Solution1()
sol1.rotate(nums, 2)
print(nums)
