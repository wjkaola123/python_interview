from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> (bool, int):
        l = []
        for i in range(len(matrix)):
            l.extend(matrix[i])

        try:
            i = l.index(target)
            return True, i
        except ValueError:
            return False, -1


s = Solution()
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 15))


class Solution2:

    def binary_search(self, l, target: int) -> bool:
        start = 0
        end = len(l) - 1

        while start <= end:
            mid = (start + end) // 2
            if l[mid] == target:
                return True
            elif l[mid] < target:
                start = mid + 1
            elif l[mid] > target:
                end = mid - 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = []
        for i in range(len(matrix)):
            l.extend(matrix[i])

        return self.binary_search(l, target)


s2 = Solution2()
print(s2.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(s2.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 15))
