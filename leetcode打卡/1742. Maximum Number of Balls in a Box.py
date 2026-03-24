import sys
from collections import Counter


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        results = [0 for _ in range(highLimit + 1)]

        for i in range(lowLimit, highLimit + 1):
            if i < 10:
                results[i] = 1
            else:
                str_list = list(str(i))
                nums = [int(str_item) for str_item in str_list]
                count = sum(nums)
                results[count] += 1

        return max(results)

    def countBalls2(self, lowLimit: int, highLimit: int) -> int:
        count = Counter(sum(map(int, str(i))) for i in range(lowLimit, highLimit + 1))
        for key, val in count.items():
            print(key, val)
        return max(count.values())

    def countBalls3(self, lowLimit: int, highLimit: int) -> int:
        for i in range(lowLimit, highLimit + 1):
            s = sum(map(int, str(i)))
            print(s)


if __name__ == '__main__':
    s = Solution()
    print(s.countBalls2(1, 12))
