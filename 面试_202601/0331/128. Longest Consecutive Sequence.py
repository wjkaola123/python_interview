from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l = sorted(list(set(nums)))
        n = len(l)
        start = 0 # 指针的起始位
        ans = 0
        count = 1  # 计数值
        for i in range(1, n):
            if l[i] == l[i - 1] + 1:
                count += 1  # 一直连续的场景
                continue
            else:
                # 不连续时, 记录最大长度
                ans = max(ans, i - start)
                start = i
                count = 1

        return max(ans, count)


s = Solution()
assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
assert s.longestConsecutive([1, 2, 6, 7, 8]) == 3
