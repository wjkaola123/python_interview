from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        times = 0
        for num in nums:
            if num == target:
                times += 1
        return times
