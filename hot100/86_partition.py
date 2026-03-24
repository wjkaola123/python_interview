class Solution:
    def partition(self, s: str) -> int:
        """
        暴力计算最长回文字符串
        :param s:
        :return:
        """
        results = []
        length = len(s)
        for i in range(length):
            for j in range(i, length):
                if self.is_palindrome(s, i, j):
                    li = []
                    li.extend(list(s[0:i]))
                    li.append(s[i: j + 1])
                    li.extend(list(s[j + 1:]))
                    if li not in results:
                        results.append(li)
        return results

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
    print(s.partition("cbbbcc"))
