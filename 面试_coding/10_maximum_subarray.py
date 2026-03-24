from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        max_nums = []
        for i in range(length):
            m = s = nums[i]
            for j in range(i + 1, length):
                s += nums[j]
                m = max(m, s)

            max_nums.append(m)

        return max(max_nums)


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))