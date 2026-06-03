from typing import List


def num_of_island(grid: List[List[str]]) -> int:
    def dfs(grid, i, j):
        if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count


grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1' , '1']
]

assert num_of_island(grid) == 3

grid1 = [
    ['1', '0', '1'],
    ['0', '1', '0'],
    ['1', '0', '1']
]

assert num_of_island(grid1) == 5