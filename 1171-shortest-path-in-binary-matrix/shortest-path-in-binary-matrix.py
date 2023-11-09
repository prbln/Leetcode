from collections import deque 

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        longestPath = -1
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] ==1:
            return -1
        q = deque() 
        q.append((0,0,1))
        visited = dict()
        rows = [-1,0,1,0,1,-1,1,-1]
        cols = [0,1,0,-1,1,-1,-1,1]
        while(len(q) != 0):
            i,j, path_length = q.popleft()
            if i == n-1 and j ==m-1:
                longestPath = max(longestPath,path_length )
            visited[(i,j)] = True
            for ind in range(8):
                newCol = j + cols[ind]
                newRow = i + rows[ind]
                if newCol<m and newCol >=0 and newRow<n and newRow>=0 and grid[newRow][newCol] ==0 and not visited.get((newRow,newCol), False):
                    visited[(newRow,newCol)] = True
                    q.append((newRow,newCol, path_length+1))
                    i
        return longestPath 
        
        


        