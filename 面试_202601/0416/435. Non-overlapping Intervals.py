from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        first = 0
        second = 1
        sort_intervals = sorted(intervals, key=lambda item: item[1])  # 选择右端点进行排序, 贪心
        ans = 0

        while second < n:
            if sort_intervals[second][0] < sort_intervals[first][1]:
                # overlapped
                del sort_intervals[second]
                ans += 1
                n -= 1
            else:
                first += 1
                second += 1

        return ans


s = Solution()
assert s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
intervals = [[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98], [-63, 2],
             [30, 47], [-40, -26]]
assert s.eraseOverlapIntervals(intervals) == 7
