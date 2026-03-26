from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for index, n in enumerate(numbers):
            if target - n in d:
                return [d[target - n], index + 1]
            else:
                d[n] = index + 1
