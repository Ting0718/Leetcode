class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = float('inf')
        for price in prices:
            min_buy = min(price, min_buy)
            profit = price - min_buy
            max_profit = max(profit, max_profit)
        return max_profit
