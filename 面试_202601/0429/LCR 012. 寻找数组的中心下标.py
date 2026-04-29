from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        left_sum = 0
        right_sum = 0

        while start < end:
            if left_sum <= right_sum:
                left_sum += nums[start]
                start += 1
            else:
                right_sum += nums[end]
                end -= 1

            if left_sum == right_sum and start == end:
                return start

        return -1


# s = Solution()
# assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
# assert s.pivotIndex([-1, -1, -1, -1, -1, 0]) == 2

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum, N = 0, sum(nums), len(nums)
        for i in range(N):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


s = Solution()
assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
assert s.pivotIndex([-1, -1, -1, -1, -1, 0]) == 2
