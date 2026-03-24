from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        使用跳跃区间的思路解法
        :param nums:
        :return:
        """
        begin = 0
        end = 0

        while end < len(nums) - 1:
            max_pos = 0
            for i in range(begin, end + 1):
                max_pos = max(max_pos, i + nums[i])

            begin = end + 1
            end = max_pos

            if begin > end:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([1, 2]))
