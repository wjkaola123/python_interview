import math


class Solution(object):
    def cuttingRope(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)


if __name__ == '__main__':
    s = Solution()
