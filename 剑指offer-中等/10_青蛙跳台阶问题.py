class Solution:
    def numWays(self, n: int) -> int:
        if n in (0, 1):
            return 1
        return self.numWays(n - 1) + self.numWays(n - 2)


class Solution1:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


if __name__ == '__main__':
    s = Solution()
    print(s.numWays(5))
