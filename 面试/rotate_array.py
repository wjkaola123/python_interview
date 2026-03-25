from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        if length <= 1:
            return

        k = k % length
        nums[:] = nums[-k:] + nums[:-k]
