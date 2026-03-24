import re


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        alist = re.findall("\d+|-\d+", s)
        s = alist[0]
        is_less_than_zero = False
        if '-' in s:
            is_less_than_zero = True
            s = s[1:]
        alist = list(s)
        length = len(alist)
        sum = 0
        for i in range(length):
            sum += int(alist[length - 1 - i]) * pow(10, i)

        return sum if not is_less_than_zero else -sum


if __name__ == '__main__':
    s = Solution()
    # assert s.myAtoi("1234") == 1234
    # assert s.myAtoi("9589") == 9589
    # assert s.myAtoi("-42") == -42
    # assert s.myAtoi("4193 with words") == 4193
    assert s.myAtoi("words and 987") == 987
