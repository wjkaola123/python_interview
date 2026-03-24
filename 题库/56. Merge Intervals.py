from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        sort_intervals = sorted(intervals)
        results = [sort_intervals[0]]
        for i in range(1, len(sort_intervals)):
            # 判断results数组最后一个区间是否和每个区间需要合并
            if sort_intervals[i][0] > results[-1][1]:
                results.append(sort_intervals[i])
            else:
                # 需要合并
                results[-1][0] = min(results[-1][0], sort_intervals[i][0])
                results[-1][1] = max(results[-1][1], sort_intervals[i][1])
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
