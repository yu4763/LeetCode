class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])
        zi = [False] * M
        zk = [False] * N
        i, k = 0, 0
        while i < M and k < N:
            if matrix[i][k] == 0:
                zi[i] = True
                zk[k] = True
            k += 1
            if k >= N:
                i += 1
                k = 0                

        for i in range(M):
            for k in range(N):
                if zi[i] or zk[k]:
                    matrix[i][k] = 0
        