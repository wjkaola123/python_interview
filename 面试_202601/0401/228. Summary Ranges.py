import copy
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 1:
            return [str(nums[0])]

        l = []
        strings = []
        # 将数组拆解为多个区间
        temp = []
        for i in range(n - 1):
            temp.append(nums[i])
            if nums[i] != nums[i + 1] - 1:
                # 中间第i+1个元素不满足连续
                l.append(temp.copy())
                temp.clear()

            if i == n - 2:  # 单独处理最后一个元素
                temp.append(nums[i + 1])
                l.append(temp.copy())

        for e in l:
            if len(e) == 1:
                strings.append(f"{e[0]}")
            else:
                strings.append(f"{e[0]}->{e[-1]}")
        return strings


s = Solution()
assert s.summaryRanges([0, 1, 2, 4, 5, 7]) == ['0->2', '4->5', '7']
assert s.summaryRanges([0, 1, 2, 4, 5, 6]) == ['0->2', '4->6']
