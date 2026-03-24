class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        暴力计算最长回文字符串
        :param s:
        :return:
        """

        length = len(s)
        if length < 2:
            return 1

        count = 0
        for i in range(length):
            for j in range(i, length):
                if self.is_palindrome(s, i, j):
                    count += 1

        return count

    def is_palindrome(self, s: str, i: int, j: int) -> bool:
        """
        判断是否回文字符串
        :param s:
        :param i:
        :param j:
        :return:
        """
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.countSubstrings("abc"))
