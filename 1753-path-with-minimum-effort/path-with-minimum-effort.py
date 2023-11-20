import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        distance = [[math.inf for j in range(m)] for i in range(n)] 
        distance[0][0] = 0
        pq = [(0, 0, 0)] #(distance, r, c)
        maxi = 0 
        while(pq):
            d, r, c = heapq.heappop(pq)
            if r ==n-1 and c ==m-1:
                return d
            neighbours = [[r+1,c], [r-1,c],[r,c+1],[r,c-1]]
            for nextr, nextc in neighbours:
                if nextr >= 0 and nextr<n and nextc>=0 and nextc<m and distance[nextr][nextc] >  d:
                    
                    distance[nextr][nextc] = max(d, abs(heights[nextr][nextc] - heights[r][c]))
                    heapq.heappush(pq, (distance[nextr][nextc], nextr, nextc ))
        return distance[-1][-1]