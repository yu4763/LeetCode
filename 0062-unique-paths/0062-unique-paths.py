import sys

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for k in range(1, n):
                memo[i][k] = memo[i-1][k] + memo[i][k-1]
        return memo[m-1][n-1]