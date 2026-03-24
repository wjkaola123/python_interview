from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        results = []
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sorted_data = sorted([nums[i], nums[j], nums[k]])
                        if sorted_data not in results:
                            results.append(sorted_data)

        return results
