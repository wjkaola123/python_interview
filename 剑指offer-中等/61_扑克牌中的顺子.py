from typing import List


class Solution:
    # 1.没有0的情况, 数字间的最大间隔只能为1
    # 2.有一个0的情况， 数字间的最大间隔可以为2
    # 3.有两个0的情况，数字间的最大间隔可以为3
    def isStraight(self, nums: List[int]) -> bool:
        length = len(nums)
        sort_nums = sorted(nums)
        zero_num = self.get_zero_num(sort_nums)
        start = zero_num
        after = start + 1
        while after < length:
            if sort_nums[after] == sort_nums[start]:
                return False
            if sort_nums[after] - sort_nums[start] > zero_num + 1:
                return False
            start += 1
            after += 1
        return True

    def get_zero_num(self, sort_nums: List[int]) -> int:
        return sort_nums.count(0)


if __name__ == '__main__':
    s = Solution()
    assert s.isStraight([11, 0, 9, 0, 0]) is True
