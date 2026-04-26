from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        s = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        t = tuple(sorted([nums[i], nums[j], nums[k]]))
                        if t not in s:
                            s.add(t)
                            ans.append([nums[i], nums[j], nums[k]])
                        else:
                            continue

        return ans
