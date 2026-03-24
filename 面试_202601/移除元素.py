from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        stack_size = 0
        for num in nums:
            if num != val:
                nums[stack_size] = num
                stack_size += 1

        return stack_size


s = Solution()
nums = [1, 1, 2, 3, 4, 1, 5, 6, 7, 8, 9]
print(s.removeElement(nums, 1))
print(nums)
