from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle

            if nums[0] <= nums[middle]:
                if nums[0] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] < target <= nums[len(nums) - 1]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
