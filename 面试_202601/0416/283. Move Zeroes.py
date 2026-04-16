from collections import OrderedDict
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        cnt = 0
        while i < n:
            if nums[i] == 0:
                del nums[i]
                cnt += 1
                n -= 1
            else:
                i += 1

        for _ in range(cnt):
            nums.append(0)


s = Solution()
nums = [0, 1, 0, 3, 12]
s.moveZeroes(nums)
assert nums == [1, 3, 12, 0, 0]
nums = [0, 0, 1]
s.moveZeroes(nums)
assert nums == [1, 0, 0]
