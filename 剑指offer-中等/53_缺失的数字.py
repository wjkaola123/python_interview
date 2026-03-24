from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        length = len(nums)
        for i in range(length + 2):
            if i not in nums:
                return i


if __name__ == '__main__':
    nums = [0, 1, 3]
    s = Solution()
    assert s.missingNumber(nums) == 2
