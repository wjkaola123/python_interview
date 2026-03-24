from typing import List


def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # 闭区间 [left, right]
    while left <= right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right+1] >= target
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1  # 范围缩小到 [left, mid-1]
        else:
            left = mid + 1  # 范围缩小到 [mid+1, right]
    # 循环结束后 left = right+1
    # 此时 nums[left-1] < target 而 nums[left] = nums[right+1] >= target
    # 所以 left 就是第一个 >= target 的元素下标
    return left


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]  # nums 中没有 target
        # 如果 start 存在，那么 end 必定存在
        end = lower_bound(nums, target + 1) - 1
        return [start, end]


s = Solution()
print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(s.searchRange(nums=[2, 2], target=2))


class Solution2:
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


s2 = Solution2()
print(s2.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(s2.searchRange(nums=[2, 2], target=2))
