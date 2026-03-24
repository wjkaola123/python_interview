import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        d = collections.Counter(nums)
        return [key for key, value in d.items() if value > length // 2][0]
