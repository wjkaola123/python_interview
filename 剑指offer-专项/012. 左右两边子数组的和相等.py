from typing import List


class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        mid = len(nums) // 2

        while True:
            # if mid < 0 or mid > len(nums) - 1:
            #     return -1
            left_nums = nums[0: mid]
            right_nums = nums[mid + 1:]
            if mid == len(nums) - 1 and sum(left_nums) != 0:
                return -1
            if mid == 0 and sum(right_nums) != 0:
                return -1
            if sum(left_nums) == sum(right_nums):
                return mid
            elif sum(left_nums) > sum(right_nums):  # 思路错了，给定的数组并非都是正数，可能为负数
                mid -= 1
            else:
                mid += 1


if __name__ == '__main__':
    s = Solution()
    assert s.pivotIndex([-1, -1, -1, -1, -1, 0]) == 2
