from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorts = sorted(points, key=lambda item: item[0])
        ans = []
        n = len(sorts)
        merge = sorts[0]
        for i in range(1, n):
            # 比较区间是否重叠
            if sorts[i][0] > merge[1]:
                # 不重叠
                ans.append(merge)
                merge = sorts[i]
            else:
                # 重叠
                left = max(sorts[i][0], merge[0])
                right = min(sorts[i][1], merge[1])
                merge = [left, right]

            if i == n - 1:
                ans.append(merge)

        return len(ans)


s = Solution()
assert s.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
