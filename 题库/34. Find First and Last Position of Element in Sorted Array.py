from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left = 0
        right = len(nums) - 1
        find_index = -1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                find_index = middle
                break
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        if find_index == -1:
            return [-1, -1]

        start_position = end_position = find_index
        while 0 <= start_position:
            if nums[start_position] == target:
                start_position -= 1
            else:
                break

        while end_position <= len(nums) - 1:
            if nums[end_position] == target:
                end_position += 1
            else:
                break

        return [start_position + 1, end_position - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
