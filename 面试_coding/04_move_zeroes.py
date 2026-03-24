from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1

        for j in range(i, len(nums)):
            nums[j] = 0

nums = [0,1,0,3,12]
sol = Solution()
sol.moveZeroes(nums)
print(nums)