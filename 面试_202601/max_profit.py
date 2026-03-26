from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        length = len(prices)
        for i in range(length):
            for j in range(i + 1, length):
                max_profit = max(max_profit, prices[j] - prices[i])

        return max_profit
