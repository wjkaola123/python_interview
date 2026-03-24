from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        sum = 0
        for index, num in enumerate(digits):
            sum += num * pow(10, length - 1 - index)
        sum += 1
        str_num = str(sum)
        return [int(n) for n in str_num]


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 2, 3]))
