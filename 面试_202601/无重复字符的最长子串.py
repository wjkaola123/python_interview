class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        left = 0
        max_len = 0
        d = {}
        for right, c in enumerate(s):
            if c not in d:
                d[c] = right
                max_len = max(max_len, right - left + 1)
            else:
                max_len = max(max_len, right - left)
                left = d[c] + 1  # 左指针移动到相同字符的下一个位置
                # index 小于当前 left的数据已失效
                d = {k: v for k, v in d.items() if v >= left}
                d[c] = right

        return max_len


s = "tmmzuxt"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
