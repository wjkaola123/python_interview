from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        d = c.most_common()
        for key, value in d:
            if value == 1:
                return key
        return None
