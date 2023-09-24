from heapq import heappop, heappush
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time_table = defaultdict(list)
        for time in times:
            node = time[0]
            time_table[node].append(time)
        
        pq = []
        min_times = {}
        heappush(pq, (0, k))

        while pq:
            cur_time, node = heappop(pq)
            if not node in min_times:
                min_times[node] = cur_time
                for (_, e, t) in time_table[node]:
                    heappush(pq, (cur_time+t, e))
        
        if len(min_times) != n:
            return -1
        return max(min_times.values())


        