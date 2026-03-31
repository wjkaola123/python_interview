from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        ans = 0
        for i in range(1, n):
            if prices[i - 1] < prices[i]:
                # 前一天买, 后一天卖
                ans += prices[i] - prices[i - 1]

        return ans
