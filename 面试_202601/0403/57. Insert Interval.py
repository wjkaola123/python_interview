from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        merged_interval = [newInterval[0], newInterval[1]]
        if not intervals:
            ans.append(merged_interval)
            return ans

        flag = 0  # 初始态
        for i in range(n):
            # 判断当前区间是否与新区间重叠
            if merged_interval[0] > intervals[i][1] or merged_interval[1] < intervals[i][0]:  # 不重叠
                if flag == 1:
                    ans.append(merged_interval)
                    flag = 2  # 已合并
                ans.append(intervals[i])
            else:
                # 重叠,合并两个区间
                flag = 1  # 合并中
                left = min(intervals[i][0], merged_interval[0])
                right = max(intervals[i][1], merged_interval[1])
                merged_interval = [left, right]

        if flag in [0, 1]:
            ans.append(merged_interval)
        ans = sorted(ans, key=lambda item: item[0])
        return ans


s = Solution()
assert s.insert([[1, 5]], [2, 3]) == [[1, 5]]
assert s.insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
