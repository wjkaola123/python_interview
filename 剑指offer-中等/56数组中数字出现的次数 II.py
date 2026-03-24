from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        d = {}
        for n in nums:
            if n not in d:
                d.update({n: 1})
            else:
                d.update({n: d[n] + 1})

        for key, val in d.items():
            if val == 1:
                return key
