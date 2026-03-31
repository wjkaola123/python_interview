from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for ind, i in enumerate(nums):
            if ind > reach:
                return False
            reach = max(reach, ind + i)  # 贪心算法,每次取可到达的最大位置

        return True
