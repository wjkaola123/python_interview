import collections
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            # 计算前缀之积
            if i == 0:
                ans.append(1)
            else:
                product = ans[i - 1] * nums[i - 1]
                ans.append(product)

        # 计算后缀之积
        queue = collections.deque()
        end = n - 1
        while end >= 0:
            if end == n - 1:
                queue.appendleft(1)
            else:
                product = nums[end + 1] * queue[0]
                queue.appendleft(product)
            end -= 1

        # 前缀之积 * 后缀之积
        for i in range(n):
            ans[i] = ans[i] * queue[i]

        return ans


s = Solution()
assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
