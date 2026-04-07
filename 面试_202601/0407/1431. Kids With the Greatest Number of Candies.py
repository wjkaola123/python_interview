from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        n = m - extraCandies
        ans = []
        for i in candies:
            if i >= n:
                ans.append(True)
            else:
                ans.append(False)

        return ans
