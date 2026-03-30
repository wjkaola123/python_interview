from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for ind, n in enumerate(nums):
            if n not in d:
                d[n] = ind
            else:
                if abs(ind - d[n]) <= k:
                    return True
                else:
                    d[n] = ind

        return False
