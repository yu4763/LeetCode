class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix) - 1
        for i in range(0, len(matrix)//2):
            for k in range(i, N-i):
                start = matrix[i][k]
                matrix[i][k] = matrix[N-k][i]
                matrix[N-k][i] = matrix[N-i][N-k] 
                matrix[N-i][N-k] = matrix[k][N-i]
                matrix[k][N-i] = start

        return matrix
        