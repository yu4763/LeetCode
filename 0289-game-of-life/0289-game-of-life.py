class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = len(board)
        M = len(board[0])


        def get(i, k):
            if 0 <= i < N and 0 <= k < M:
                return board[i][k]
            else:
                return 0
        
        def calculate(i, k):
            return (
                get(i-1, k-1) + get(i-1, k) + get(i-1, k+1) + 
                get(i, k-1) + get(i, k+1) +
                get(i+1, k-1) + get(i+1, k) + get(i+1, k+1)
            )

        change = []
        for i in range(N):
            for k in range(M):
                if board[i][k] == 0 and calculate(i, k) == 3:
                    change.append((i, k))
                if board[i][k] == 1 and calculate(i, k) not in (2, 3):
                    change.append((i, k))
        
        for c in change:
            i = c[0]
            k = c[1]
            if board[i][k]:
                board[i][k] = 0
            else:
                board[i][k] = 1
            