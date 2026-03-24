class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0:
            n_plus = abs(n)
        else:
            n_plus = n
        for i in range(n_plus):
            if n_plus == 0:
                return res
            res *= x
        if n < 0:
            res = 1 / res
        return res

    def myPow2(self, x: float, n: int) -> float:
        return x ** n


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.0, 10))
