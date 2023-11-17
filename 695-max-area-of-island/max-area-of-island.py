class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        n = len(grid)
        m = len(grid[0])
        visited = dict()
        def dfs(stack):
            
            count = 0 
            while(len(stack)!= 0 ):
                i, j = stack.pop()
                visited[(i, j)] = True
                count+=1 
                nextEle = [[0,1],[0,-1],[1,0],[-1,0]]
                for r,c in nextEle:
                    nextr = i + r
                    nextc = j + c
                    if min(nextr, nextc) >=0 and nextr<n and nextc<m and grid[nextr][nextc] == 1 and not visited.get((nextr, nextc), False):
                        stack.append((nextr, nextc))
                        visited[(nextr, nextc)] = True
            return count
        for i in range(n):
            for j in range(m):
                if grid[i][j] ==1 and not visited.get((i,j), False):
                    area = dfs([(i,j)])
                    maxArea = max(maxArea, area )

        return maxArea
         