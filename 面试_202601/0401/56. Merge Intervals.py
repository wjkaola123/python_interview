from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 首先对区间第一个元素从小到大排序
        ans = []
        sorts = sorted(intervals, key=lambda item: item[0])
        n = len(sorts)
        temp = sorts[0]
        for i in range(1, n):
            if temp[1] >= sorts[i][0]:  # 满足合并条件
                right = max(temp[1], sorts[i][1])
                temp = [temp[0], right]
            else:
                ans.append(temp)
                temp = sorts[i]

        ans.append(temp)
        return ans


s = Solution()
intervals = [[4, 7], [1, 4]]
print(s.merge(intervals))

intervals_1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(s.merge(intervals_1))

intervals_2 = [[1, 4], [2, 3], [4, 9]]
print(s.merge(intervals_2))
