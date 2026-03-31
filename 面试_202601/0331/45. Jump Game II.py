from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_pos, end, step = 0, 0, 0
        for i in range(n - 1):
            max_pos = max(max_pos, i + nums[i])
            if i == end:  # 正向求解, 每次走最远的距离, 得到最小的步数
                end = max_pos
                step += 1

        return step


nums = [2, 3, 1, 1, 4]
s = Solution()
assert s.jump(nums) == 2
