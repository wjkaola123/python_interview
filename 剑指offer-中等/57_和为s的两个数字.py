from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [nums[i], nums[j]]

    def two_point(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1

        while i != j:
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
            elif nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 26))
