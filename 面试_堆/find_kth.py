from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(Solution().findKthLargest(nums, k))


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]


print("*" * 30)
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(Solution2().findKthLargest(nums, k))
