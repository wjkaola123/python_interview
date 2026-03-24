from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        results = []

        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res = sorted([nums[i], nums[j], nums[k]])
                        if res not in results:
                            results.append(res)

        return results


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([0, 1, 1]))
