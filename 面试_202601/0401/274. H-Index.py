from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        ans = 0
        for i in range(n):
            if citations[i] == 0:  # paper引用次数为0,不需要进行统计
                continue

            c = 0
            for j in range(n):
                if citations[j] >= citations[i]:
                    c += 1  # 统计一共有多少篇paper是大于等于当前引用数

            if c >= citations[i]:
                ans = max(ans, citations[i])  # paper数大于等于当前引用数,则用引用数更新 ans
            else:
                ans = max(ans, c)  # paper数小于当前引用数, 则用paper数更新ans
        return ans


citations = [3, 0, 6, 1, 5]
s = Solution()
assert s.hIndex(citations) == 3
assert s.hIndex([100]) == 1
assert s.hIndex([3, 0, 6, 1, 5, 7]) == 3
