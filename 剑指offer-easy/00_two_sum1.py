from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i

        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
