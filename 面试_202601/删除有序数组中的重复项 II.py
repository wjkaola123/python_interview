from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                if d[nums[i]] == 1:
                    nums[k] = nums[i]
                    k += 1
                    d[nums[i]] = 2
            else:
                d[nums[i]] = 1
                nums[k] = nums[i]
                k += 1

        nums[:] = nums[:k]
        return k


nums = [1, 1, 1, 2, 2, 3]

k = Solution().removeDuplicates(nums)
print(nums, k)
