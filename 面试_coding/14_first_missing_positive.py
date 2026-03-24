from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums[:] = sorted(nums)
        min_num = min(nums)
        max_num = max(nums)

        # If the smallest num is larger than 1 or the maximum num is less than 1
        if min_num > 1 or max_num < 1:
            return 1

        n = len(nums)
        for i in range(n):
            if nums[i] <= 1:
                continue
            else:
                if nums[i] - nums[i - 1] > 1:
                    if nums[i - 1] <= 0:
                        return 1
                    else:
                        return nums[i - 1] + 1

                if i + 1 < n and nums[i + 1] - nums[i] > 1:
                    return nums[i] + 1

        return nums[n - 1] + 1


nums = [7, 8, 9, 11, 12]
print(Solution().firstMissingPositive(nums))

nums = [1, 2, 0]
print(Solution().firstMissingPositive(nums))

nums = [3, 4, -1, 1]
print(Solution().firstMissingPositive(nums))

nums = [-1, -2, -60, 40, 43]
print(Solution().firstMissingPositive(nums))
