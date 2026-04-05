class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            if buy < sell:
                profit = max(profit, sell - buy)
                r += 1
            else:
                l = r
                r += 1
        return profit