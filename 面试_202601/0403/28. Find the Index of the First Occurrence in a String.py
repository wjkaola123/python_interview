class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        m = len(needle)

        for i in range(n):
            if haystack[i] == needle[0]:  # 第一个字符相同时, 比较m个字符
                if haystack[i: i + m] == needle:
                    return i

        return -1


s = Solution()
assert s.strStr("sadbutsad", "but") == 3
