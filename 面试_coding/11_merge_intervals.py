# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        results = [sorted_intervals[0]]
        length = len(sorted_intervals)

        for i in range(1, length):
            if results[-1][1] < sorted_intervals[i][0]:
                results.append(sorted_intervals[i])
            else:
                # need merging
                results[-1][0] = min(results[-1][0], sorted_intervals[i][0])
                results[-1][1] = max(results[-1][1], sorted_intervals[i][1])

        return results


intervals = [[4, 7], [1, 4]]
result = Solution().merge(intervals)
print(result)
