class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        N = len(prices)
        
        base = prices[0]
        for i in range(1, N):
            print(i, base, profits)
            if prices[i] <= base:
                base = prices[i]
            elif i == N-1:
                profits += prices[i] - base
                base = prices[i]
            elif prices[i + 1] >= prices[i]:
                continue
            else:
                profits += prices[i] - base
                base = prices[i]

        return profits

        