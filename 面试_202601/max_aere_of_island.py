from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0:
                return 0

            grid[i][j] = 0 # 设置标记
            area = 1
            area += dfs(grid, i + 1, j)  # 下
            area += dfs(grid, i - 1, j)  # 上
            area += dfs(grid, i, j + 1)  # 右
            area += dfs(grid, i, j - 1)  # 左
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = dfs(grid, i, j)
                    max_area = max(max_area, ans)

        return max_area
