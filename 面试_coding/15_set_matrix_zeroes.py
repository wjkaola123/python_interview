from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_indexes = set()
        col_indexes = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row_indexes.add(i)
                    col_indexes.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in row_indexes:
                    matrix[i][j] = 0
                if j in col_indexes:
                    matrix[i][j] = 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(matrix)
Solution().setZeroes(matrix)
print(matrix)

# test
# arr = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(f"a[{i}][{j}]={arr[i][j]}")


