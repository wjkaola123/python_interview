import heapq
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int):

        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap

    def findKthLargest2(self, nums: List[int], k: int):
        heap = []
        for num in nums:
            if len(heap) >= k:
                if num > heap[0]:
                    heapq.heapreplace(heap, num)
            else:
                heapq.heappush(heap, num)

        return heap

nums = list(range(1000))
random.shuffle(nums)
ret1 = Solution().findKthLargest(nums, 5)
print(ret1)
ret2 = Solution().findKthLargest2(nums, 5)
print(ret2)
assert set(ret1) == set(ret2)
