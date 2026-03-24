import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        return [key for key, value in d.items() if value == 1][0]


Solution().singleNumber([1, 2, 2, 3, 3])
