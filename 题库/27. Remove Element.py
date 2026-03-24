from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        point = 0

        while point < len(nums):
            if nums[point] == val:
                nums.pop(point)
                point -= 1
            point += 1

        return len(nums)
