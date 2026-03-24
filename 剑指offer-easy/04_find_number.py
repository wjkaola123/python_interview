from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for list_item in matrix:
            for item in list_item:
                if item == target:
                    return True

        return False


if __name__ == '__main__':
    pass
