from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        nums = [i for i in range(1, target)]
        results = []

        for i in range(target):
            s = 0
            num_list = []
            for j in range(i, len(nums)):
                if s < target:
                    num_list.append(nums[j])
                    s += nums[j]
                elif s == target:
                    results.append(num_list)
                    break
                elif s > target:
                    break
        return results
