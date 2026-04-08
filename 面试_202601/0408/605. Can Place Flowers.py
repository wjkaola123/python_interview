from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # 利用三个指针统计可种花的数目
        first = 0
        middle = 1
        end = 2
        length = len(flowerbed)
        ans = 0
        if length == 1 and flowerbed[0] == 0:
            flowerbed[0] = 1
            ans += 1
        elif length == 2 and flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            ans += 1
        # 处理中间位置
        while end <= length - 1:
            if first == 0:  # 起始位置
                if flowerbed[first] == 0 and flowerbed[middle] == 0:
                    flowerbed[first] = 1
                    ans += 1

            if end == length - 1:  # 结束位置
                if flowerbed[length - 2] == 0 and flowerbed[length - 1] == 0:
                    flowerbed[length - 1] = 1
                    ans += 1

            if flowerbed[first] == 0 and flowerbed[middle] == 0 and flowerbed[end] == 0:  # 中间位置
                flowerbed[middle] = 1
                ans += 1

            first += 1
            middle += 1
            end += 1

        return ans >= n
