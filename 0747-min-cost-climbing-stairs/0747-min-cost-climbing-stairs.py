class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)

        memo = {0:0, 1:0}
        def getCost(n):
            if n in memo:
                return memo[n]
            
            minCost = min(getCost(n-1) + cost[n-1], getCost(n-2) + cost[n-2])
            memo[n] = minCost
            return minCost
        
        return getCost(N)

        