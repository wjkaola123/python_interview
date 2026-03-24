from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        print(nums)
        return max(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -1, 4]
    print(s.maxSubArray(nums))
