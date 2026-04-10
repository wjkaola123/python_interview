import collections
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answers = []
        n = len(nums)
        for i in range(n):
            if i == 0:
                answers.append(1)
            else:
                ans = answers[i - 1] * nums[i - 1]
                answers.append(ans)

        suffix_ans = collections.deque()
        end = n - 1
        while end >= 0:
            if end == n - 1:
                suffix_ans.appendleft(1)
            else:
                ans = suffix_ans[0] * nums[end + 1]
                suffix_ans.appendleft(ans)
            end -= 1
        for i in range(n):
            answers[i] = answers[i] * suffix_ans[i]

        return answers
