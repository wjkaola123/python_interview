from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


s = Solution()
nums = [-1, 0, 0, 0, 0, 3, 3]
k = s.removeDuplicates(nums)
print(nums, k)
