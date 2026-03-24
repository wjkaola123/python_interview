from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        width = len(height)
        max_container = 0
        for index, h in enumerate(height):
            for w in range(index + 1, width):
                select_width = w - index
                contain = min(h, height[w]) * select_width
                max_container = max(max_container, contain)


        return max_container



heights = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(heights))