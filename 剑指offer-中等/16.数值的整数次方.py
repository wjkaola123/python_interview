class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n < 0:
            plus_n = abs(n)
        else:
            plus_n = n
        for i in range(plus_n):
            result *= x

        if n < 0:
            result = 1 / result
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.0, 10))
    print(pow(2, 3))
    print(2 ** 5)
