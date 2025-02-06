class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        profits = 0
        base = prices[0]
        
        for i in range(1, N):
            if base < prices[i]:
                profits += prices[i] - base
            base = prices[i]
        return profits

        