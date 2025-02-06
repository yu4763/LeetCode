class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        max_values = [0] * N
        max_values[N-1] = prices[N-1]
        for i in range(N-2, -1, -1):
            max_value = max(max_values[i+1], prices[i])
            max_values[i] = max_value
        
        max_profit = 0
        for i in range(N):
            profit = max_values[i] - prices[i]
            if profit > max_profit:
                max_profit = profit
        
        return max_profit



    


        