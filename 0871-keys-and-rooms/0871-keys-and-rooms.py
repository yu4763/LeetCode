from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited = [False] * N

        queue = deque([0])
        visited[0] = True

        while queue:
            num = queue.popleft()
            keys = rooms[num]
            for key in keys:
                if not visited[key]:
                    queue.append(key)
                    visited[key] = True
        
        return all(visited)



        