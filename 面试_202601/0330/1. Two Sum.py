from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for ind, n in enumerate(nums):
            sec_num = target - n
            if sec_num not in d:
                d[n] = ind
            else:
                return [ind, d[sec_num]]
