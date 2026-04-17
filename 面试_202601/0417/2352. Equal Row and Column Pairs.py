from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        grid_col = [[0] * m for _ in range(n)]
        for i, g in enumerate(grid):
            for j, x in enumerate(g):
                grid_col[j][i] = x

        for g in grid:
            for c in grid_col:
                if g == c:
                    ans += 1

        return ans


grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]

s = Solution()
assert s.equalPairs(grid) == 1
