from math import inf
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        ans = 0
        n = len(gain)
        for i in range(n):
            if i == 0:
                altitudes.append(gain[i])
            else:
                altitude = altitudes[-1] + gain[i]
                altitudes.append(altitude)

            ans = max(ans, altitudes[-1])

        return ans
