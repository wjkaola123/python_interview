from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        count, last1, last2 = 0, -1, -1

        for index, n in enumerate(nums):
            if n >= left and n <= right:
                last1 = index
            if n > right:
                last2 = index
                last1 = -1

            if last1 != -1:
                count += last1 - last2

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.numSubarrayBoundedMax([73, 55, 36, 5, 55, 14, 9, 7, 72, 52], 32, 69))
