from typing import List


class Solution:

    def getOneNums(self, n: int):
        temp, count = 0, 0
        while n != 0:
            temp = n % 2
            n = n // 2
            if temp == 1:
                count += 1
        return count

    def countBits(self, n: int) -> List[int]:
        counts = []
        for i in range(n + 1):
            c = self.getOneNums(i)
            counts.append(c)

        return counts


if __name__ == '__main__':
    s = Solution()
    assert s.getOneNums(0) == 0
    assert s.getOneNums(1) == 1
    assert s.getOneNums(2) == 1
    assert s.getOneNums(3) == 2
    assert s.getOneNums(4) == 1
    assert s.getOneNums(5) == 2
    assert s.getOneNums(6) == 2
    assert s.getOneNums(7) == 3
    assert s.getOneNums(8) == 1
