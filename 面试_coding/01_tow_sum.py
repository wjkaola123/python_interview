# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
from copy import deepcopy
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            add_nums = nums[idx + 1:]
            for idx2, num2 in enumerate(add_nums):
                if num + num2 == target:
                    return [idx, idx + 1 + idx2]
        return []
