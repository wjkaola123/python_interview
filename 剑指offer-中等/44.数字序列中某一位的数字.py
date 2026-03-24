import sys


class Solution:
    def findNthDigit(self, n: int) -> int:
        tmp = ''
        for i in range(n + 1):
            tmp += str(i)
        alist = list(tmp)
        return int(alist[n])


if __name__ == '__main__':
    s = Solution()
    print(s.findNthDigit(3))
