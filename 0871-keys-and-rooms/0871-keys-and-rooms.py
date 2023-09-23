from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited = [False] * N

        def dfs(num):
            keys = rooms[num]
            for key in keys:
                if not visited[key]:
                    visited[key] = True
                    dfs(key)
        
        visited[0] = True
        dfs(0)

        return all(visited)

        