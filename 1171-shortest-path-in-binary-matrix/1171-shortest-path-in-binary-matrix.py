from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] != 0 or grid[N-1][N-1] != 0:
            return -1

        visited = [[False]*N for _ in range(N)]
        queue = deque([(0, 0, 1)])
        visited[0][0] = True
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, +1, +1, +1, 0, -1, -1]

        while queue:
            x, y, length = queue.popleft()
            if x == N-1 and y == N-1:
                return length

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < N and 0 <= ny < N):
                    if grid[nx][ny] == 0 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, length+1))
        
        return -1

        
    