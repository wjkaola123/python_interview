import math


class Solution(object):
    def cuttingRope(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            result = int(math.pow(3, a))
        if b == 1:
            result = int(math.pow(3, a - 1) * 4)
        if b == 2:
            result = int(math.pow(3, a) * 2)
        if result > 1000000007:
            result = result % 1000000007
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.cuttingRope(120))
