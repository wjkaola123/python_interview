from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l = sorted(list(set(nums)))
        n = len(l)
        start = 0  # 指针的起始位
        end = 0  # 指针的结束位
        ans = 0
        for i in range(1, n):
            end += 1
            if l[i] == l[i - 1] + 1:
                continue
            else:
                # 不连续时, 记录最大长度
                ans = max(ans, end - start)
                start = i

        return max(ans, end - start + 1)


s = Solution()
assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
assert s.longestConsecutive([1, 2, 6, 7, 8]) == 3
