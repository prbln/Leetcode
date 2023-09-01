from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        n = len(grid)
        m = len(grid[0])
        visited = dict()
        noFresh = True
        for i in range(n):
            for j in range(m):
                if grid[i][j] ==2:
                    q.append([i,j])
                if grid[i][j] ==1:
                    noFresh = False
        def BFS(queue, visted):
            minute=0
            while(len(queue)!=0):
                minute+=1
                print(queue)
                for i in range(len(queue)):
                    r,c = queue.popleft()
                    visited[(r,c)] = True
                    # if grid[r][c] == 2:

                    adjRow = [-1,0,1,0]
                    adjCol = [0,-1,0,1]
                    for i in range(4):
                        nxtRow = r + adjRow[i]
                        nxtCol = c + adjCol[i]
                        if nxtRow<n and nxtRow>=0 and nxtCol<m and nxtCol>=0 and not visited.get((nxtRow,nxtCol), False) and grid[nxtRow][nxtCol] !=0:
                            # print(nxtRow,nxtCol )
                            grid[nxtRow][nxtCol] =2
                            queue.append([nxtRow, nxtCol])
                            visited[(nxtRow,nxtCol)] = True
            return minute              
        if noFresh:
            return 0
        ans = BFS(q,visited) -1
        # print(ans)
        for i in range(n):
            for j in range(m):
                if grid[i][j] ==1:
                    return -1 
        return ans

        
        
        