from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        q = deque()
        visited = [[0 for j in range(m)] for i in range(n)]
        numOfFresh = 0 
        time = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                elif grid[i][j] == 1:
                    numOfFresh+=1
        while(len(q)!= 0):
            r,c,t = q.popleft()
            visited[r][c] = True
            time =max(t, time)
            if grid[r][c] == 1:
                numOfFresh-=1
            nextEle =[[-1,0],[1,0],[0,-1],[0,1]]
            for i,j in nextEle:
                nextRow = i + r
                nextCol = j + c
                if min(nextRow,nextCol )>=0 and nextRow<n and nextCol<m and grid[nextRow][nextCol] == 1 and not visited[nextRow][nextCol] :
                    q.append((nextRow,nextCol,t+1))
                    visited[nextRow][nextCol] = True
        if numOfFresh >0:
            return - 1
        return time


                
            