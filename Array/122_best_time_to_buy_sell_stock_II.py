class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):  # start from 1 bc 0 can't compare to previous
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
