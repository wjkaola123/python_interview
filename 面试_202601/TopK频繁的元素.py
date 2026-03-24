"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        collection = collections.Counter(nums)
        sorted_dict = sorted(collection.items(), key=lambda x: x[1], reverse=True)
        return [i[0] for i in sorted_dict[:k]]


ret = Solution().topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2, 0, 0, 0, 0, 0, 2], 2)
print(ret)
