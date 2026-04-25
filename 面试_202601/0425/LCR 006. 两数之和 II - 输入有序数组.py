from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for ind, n in enumerate(numbers):
            sec = target - n
            if sec in d:
                return [d[sec], ind]
            else:
                d[n] = ind
