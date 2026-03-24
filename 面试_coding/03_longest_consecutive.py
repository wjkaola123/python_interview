from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = list(sorted(set(nums)))
        current_index = 1
        max_length = 0
        first_index = 0

        if len(arr) == 1:
            return 1

        while current_index < len(arr):
            if arr[current_index - 1] == arr[current_index] - 1:
                current_index += 1
                current_length = current_index - first_index
                max_length = max(max_length, current_length)
            else:
                length = current_index - first_index
                max_length = max(max_length, length)
                first_index = current_index
                current_index += 1

        return max_length


nums = [100,4,200,1,3,2]

sol = Solution()
print(sol.longestConsecutive(nums))
