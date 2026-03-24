from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        temp_arr = sorted(arr)
        return temp_arr[0: k]


if __name__ == '__main__':
    pass
