from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1

        max_area = 0
        while start < end:
            cur_height = min(height[start], height[end])
            cur_width = end - start
            max_area = max(max_area, cur_height * cur_width)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area
