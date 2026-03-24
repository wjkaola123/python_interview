class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        else:
            return self.numWays(n - 1) + self.numWays(n - 2)

    def numWays2(self, n):
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


if __name__ == '__main__':
    s = Solution()
    print(s.numWays(10))
    print(s.numWays2(10))
