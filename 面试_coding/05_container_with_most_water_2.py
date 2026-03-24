from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1

        max_area = 0
        while start < end:
            current_height = min(height[start], height[end])
            current_width = end - start
            current_area = current_height * current_width
            max_area = max(max_area, current_area)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area

heights = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(heights))