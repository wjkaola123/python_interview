import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = nums
        heapq.heapify(self.h)
        # 关键修正：如果堆元素超过 k，就弹出最小的，直到只剩 k 个
        while len(self.h) > self.k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        while len(self.h) > self.k:
            heapq.heappop(self.h)

        return self.h[0]


k = KthLargest(3, [4, 5, 8, 2])
assert k.add(3) == 4
assert k.add(5) == 5
assert k.add(10) == 5
assert k.add(9) == 8
assert k.add(4) == 8
