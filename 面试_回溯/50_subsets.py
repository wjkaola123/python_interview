from typing import List

"""
子集型回溯
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        # 选或不选：讨论 nums[i] 是否加入 path
        def dfs(i):
            if i == n:  # 子集构造完毕
                ans.append(path.copy())  # 复制 path，也可以写 path[:]
                return

            # 选
            path.append(nums[i])  # 选 nums[i]
            dfs(i + 1)  # 考虑下一个数 nums[i+1] 选或不选

            # 不选
            path.pop()
            dfs(i + 1)  # 不选 nums[i], 考虑下一个数 nums[i+1] 选或不选

        dfs(0)
        return ans


nums = [1, 2, 3]
print(Solution().subsets(nums))
