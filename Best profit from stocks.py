class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_index = prices.index(min(prices))
        max_index = prices.index(max(prices[min_index:]))
        profit = prices[max_index] - prices[min_index]
        if profit > 0:
            return profit
        return 0


