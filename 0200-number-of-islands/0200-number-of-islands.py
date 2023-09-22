from collections import Counter

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        visited = [[0]*N for _ in range(M)]

        def bfs(si, sk):
            queue = deque([(si, sk)])
            dx = [-1, 0, +1, 0]
            dy = [0, +1, 0, -1]
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if ( 0 <= nx < M and 0 <= ny < N):
                        if grid[nx][ny]=="1" and not visited[nx][ny] :
                            visited[nx][ny] = 1
                            queue.append((nx, ny))

        nums = 0
        for i in range(M):
            for k in range(N):
                if grid[i][k]=="1" and not visited[i][k]:
                    visited[i][k] = 1
                    nums += 1
                    bfs(i, k)
        
        return nums


        