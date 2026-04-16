from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # the max value of left and the min value of right
        n = len(points)
        ans = []
        sorted_points = sorted(points, key=lambda p: p[0])
        cur = 0
        while cur < n:
            if not ans:
                ans.append(sorted_points[cur])
                cur += 1
                continue
            # judge intervals
            if sorted_points[cur][0] <= ans[-1][1]:
                # overlapped
                ans[-1] = [max(sorted_points[cur][0], ans[-1][0]), min(sorted_points[cur][1], ans[-1][1])]
            else:
                ans.append(sorted_points[cur])
            cur += 1

        return len(ans)

s = Solution()
assert s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2