import datetime


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def fib2(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


if __name__ == '__main__':
    s = Solution()

    t1 = datetime.datetime.now()
    s.fib(38)
    t2 = datetime.datetime.now()
    deltat_sec = (t2 - t1).seconds
    print("秒:" + str(deltat_sec))
    s.fib2(50)
    t3 = datetime.datetime.now()
    deltat_ms = (t3 - t2).microseconds / 1000
    print("毫秒:" + str(deltat_ms))
