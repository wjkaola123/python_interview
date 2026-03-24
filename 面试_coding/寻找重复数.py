import collections
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        return [key for key, value in d.items() if value > 1][0]
