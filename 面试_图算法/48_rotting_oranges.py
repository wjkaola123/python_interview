"""
You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    fresh += 1  # 统计新鲜橘子个数
                elif x == 2:
                    q.append((i, j))  # 一开始就腐烂的橘子

        ans = 0
        while q and fresh:
            ans += 1
            tmp = q
            q = []
            for x, y in tmp:
                for i, j in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:  # 新鲜的橘子
                        fresh -= 1
                        grid[i][j] = 2
                        q.append((i, j))

        return -1 if fresh else ans


"""
方案二: 通过BFS队列实现
"""


class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col, time = len(grid), len(grid[0]), 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = []

        # 1. 找出腐烂橘子的位置
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j, time))

        # BFS
        while queue:
            i, j, time = queue.pop(0)
            for dx, dy in directions:  # 向上下左右各方向走一步, 检查是否存在fresh的橘子, 并设置为rotten.
                if 0 <= i + dx < row and 0 <= j + dy < col and grid[i + dx][j + dy] == 1:
                    grid[i + dx][j + dy] = 2
                    queue.append((i + dx, j + dy, time + 1))

        # 还有Fresh的,返回 -1
        for row in grid:
            if 1 in row:
                return -1

        return time
