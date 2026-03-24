from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        point = 0
        point_next = 1

        while point_next < len(nums):
            if nums[point] == nums[point_next]:
                nums.pop(point_next)
                point -= 1
                point_next -= 1

            point += 1
            point_next += 1

        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
