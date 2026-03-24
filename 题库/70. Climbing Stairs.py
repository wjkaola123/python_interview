class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        alist = [0 for _ in range(n + 1)]
        alist[1] = 1
        alist[2] = 2
        for i in range(3, n + 1):
            alist[i] = alist[i - 1] + alist[i - 2]
        return alist[n]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
