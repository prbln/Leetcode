import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = dict()
        distance = [math.inf for i in range(n)]
        distance[k-1] =0
        time = 0 
        pq = []
        heapq.heapify( pq)
        heapq.heappush(pq, [time, k])
        for u, v, w in times:
            if not adj_list.get(u, False):
                adj_list[u] = []
            if not adj_list.get(v, False):
                adj_list[v] = []
            adj_list[u].append((v,w))
        while(pq):
            Totaltime, node = heappop(pq)
            for neigh, time in adj_list[node]:
                if distance[neigh-1] > Totaltime + time:
                    distance[neigh-1] = Totaltime + time
                    heapq.heappush(pq, [distance[neigh-1], neigh])
        if max(distance) == math.inf:
            return -1 
        return max(distance)