class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        s, e = 0, 1

        while e < len(prices):
            if prices[e] > prices[s]:
                profit = prices[e] - prices[s]
                max_profit = max(profit, max_profit)
            else:
                s = e
            e += 1

        return max_profit
            