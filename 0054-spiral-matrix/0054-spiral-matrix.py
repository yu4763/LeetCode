class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def should_change(found, i, k, di):
            cur = direction[di]
            ni = cur[0] + i 
            nk = cur[1] + k 
            if (0 <= ni < M) and (0 <= nk < N):
                if not found[ni][nk]:
                    return False
            return True

        
        M = len(matrix)
        N = len(matrix[0])
        i, k = 0, 0

        found = [[False for _ in range(N)] for _ in range(M)]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        di = 0
        result = []
        while (0 <= i < M) and (0 <= k < N) and not found[i][k]:
            found[i][k] = True
            result.append(matrix[i][k])
            cur = direction[di]
            if should_change(found, i, k, di):
                di  = (di + 1) % 4
        
            cur = direction[di]
            i += cur[0]
            k += cur[1]
            
        return result

        