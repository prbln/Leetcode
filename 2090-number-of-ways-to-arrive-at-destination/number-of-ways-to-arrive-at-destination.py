import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        if n==1:
            return 1
        distance = [math.inf for i in range(n)]
        distance[0] = 0 
        num = [0 for i in range(n)]
        num[0] = 1
        pq = []
        heapq.heapify(pq)
        heapq.heappush(pq, [0,0])
        adj_list = dict()
        for u, v, time in roads:
            if not adj_list.get(u, False):
                adj_list[u] = []
            if not adj_list.get(v, False):
                adj_list[v] = []
            adj_list[u].append([v, time])
            adj_list[v].append([u, time])
        ans = 0 
        while(pq):
            TotalTime, node = heapq.heappop(pq)
            for neigh, time in adj_list[node]:
                if distance[neigh] == TotalTime + time:
                    num[neigh]+=num[node]
                
                if distance[neigh] >  TotalTime + time:
                    distance[neigh] = TotalTime + time
                    num[neigh] = num[node]
                    heapq.heappush(pq,[distance[neigh],neigh ])
        # print(num)
        return num[-1]%1000000007
