class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        if not s:
            return ''
        if n < len(s):
            tmp = s[: n]
            start = s[n:]

            return start + tmp


if __name__ == '__main__':
    s = Solution()
    print(s.reverseLeftWords("abcdefg", 2))
