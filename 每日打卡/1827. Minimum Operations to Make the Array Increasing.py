from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 临近的两个数进行比较，计算增加次数
        if len(nums) == 1:
            return 0

        point = 0
        point_next = 1
        sum = 0
        while point_next < len(nums):
            if nums[point_next] <= nums[point]:
                sum += (nums[point] - nums[point_next] + 1)  # 统计增加次数
                nums[point_next] = nums[point] + 1  # 更新后数为前数加1
            point += 1
            point_next += 1
        return sum


s = Solution()
print(s.minOperations([1, 1, 1]))
print(s.minOperations([1, 5, 2, 4, 1]))
print(s.minOperations([8]))
