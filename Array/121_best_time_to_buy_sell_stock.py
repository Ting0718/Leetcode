class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = float('inf')
        for price in prices:
            min_buy = min(price, min_buy)
            profit = price - min_buy
            max_profit = max(profit, max_profit)
        return max_profit

'''Brute Force'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                current_profit = prices[j] - prices[i]
                max_profit = max(max_profit, current_profit)

        return max_profit
