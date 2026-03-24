class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        is_positive = True if n > 0 else False
        n = abs(n)

        res = 1
        for _ in range(n):
            res *= x

        return res if is_positive else 1 / res
