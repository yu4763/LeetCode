from heapq import heappop, heappush
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time_table = defaultdict(list)
        for s, e, t in times:
            time_table[s].append((t, e))
        
        heap = [(0, k)]
        min_times = {}

        while heap:
            cur_time, node = heappop(heap)
            if not node in min_times:
                min_times[node] = cur_time
                if len(min_times) == n:
                    return max(min_times.values())
                for (t, e) in time_table[node]:
                    heappush(heap, (cur_time+t, e))
        
        return -1


        