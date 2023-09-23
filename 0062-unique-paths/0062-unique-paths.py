class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        maxV = max(m-1, n-1)
        minV = min(m-1, n-1)
        start = m+n-2
        result = 1

        for i in range(start, maxV, -1):
            result *= i
        
        for i in range(minV, 0, -1):
            result  = result // i
        
        return result