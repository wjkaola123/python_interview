from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        n = len(candidates)
        path = []
        ans = []

        def dfs(i, left):

            # 考虑递归终止条件一: 找到 path, left值为 0.
            if left == 0:
                ans.append(path.copy())
                return

            # 考虑递归终止条件二: 未找到path, 所有的 candidate 已经搜索 或是 left < 0
            if i == n or left < 0:
                return

            # 选
            path.append(candidates[i])
            dfs(i, left - candidates[i])

            # 不选
            path.pop()
            dfs(i + 1, left)

        dfs(0, target)
        return ans

s = Solution()
print(s.combinationSum([2, 3, 5], 7))




