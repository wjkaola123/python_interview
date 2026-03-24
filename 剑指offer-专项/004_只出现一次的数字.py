from typing import List, Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n not in d:
                d.update({n: 1})
            else:
                d.update({n: d[n] + 1})

        for key, value in d.items():
            if value == 1:
                return key


if __name__ == '__main__':
    s = Solution()
    assert s.singleNumber([2, 2, 3, 2]) == 3
