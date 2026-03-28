from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        d = defaultdict(int)  # 需要一个default dict 存储数据
        for right, c in enumerate(s):
            d[c] += 1
            while d[c] > 1:
                d[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
