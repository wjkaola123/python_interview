from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        start = 0
        end = n - 1
        max_area = 0

        while start < end:
            w = end - start
            h = min(height[start], height[end])
            area = w * h
            max_area = max(max_area, area)
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1

        return max_area
