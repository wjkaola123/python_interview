from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        length = len(nums)
        d = {}
        for n in nums:
            if n not in d:
                d.update({n: 1})
                count = 1
            else:
                count = d.get(n) + 1
                d.update({n: count})
            if count > (length // 2):
                return n


if __name__ == '__main__':
    nums = [1]
    s = Solution()
    print(s.majorityElement(nums))
