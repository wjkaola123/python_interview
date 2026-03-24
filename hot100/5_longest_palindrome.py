class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        暴力计算最长回文字符串
        :param s:
        :return:
        """

        length = len(s)
        if length < 2:
            return s

        max_length = 1
        begin = 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                if j - i + 1 > max_length and self.is_palindrome(s, i, j):
                    max_length = j - i + 1
                    begin = i
        return s[begin: begin + max_length]

    def is_palindrome(self, s: str, i: int, j: int) -> bool:
        """
        判断是否回文字符串
        :param s:
        :param i:
        :param j:
        :return:
        """
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
