class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0
        min_value = prices[0]

        for i in range(1, len(prices)):
            min_value = min(prices[i], min_value)
            max_value = max(prices[i] - min_value, max_value)

        return max_value



    


        