from typing import List


def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return lower_bound(nums, target)


s = Solution()
ans = s.searchInsert([1, 3, 5, 6], 5)
print(ans)

ans = s.searchInsert([1, 3, 5, 6], 2)
print(ans)

ans = s.searchInsert([1,1,3,3,5], 4)
print(ans)