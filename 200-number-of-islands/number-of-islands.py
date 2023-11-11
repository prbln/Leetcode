class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = dict()
        stack = []
        def dfs(stack):
            while(len(stack) != 0 ):
                i, j = stack.pop()
                visited[(i,j)] = True
                nextEle = [[-1,0],[1,0],[0,-1],[0,1]]
                for r,c in nextEle:
                    nextR = i + r
                    nextC = j + c
                    if nextR < n and nextC < m and min(nextR, nextC)>=0 and not visited.get((nextR, nextC), False) and grid[nextR][nextC] ==   "1":
                        stack.append((nextR, nextC)) 
                        visited[(nextR, nextC)] = True
        count = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] =="1" and not visited.get((i,j), False):
                    stack.append((i,j))
                    visited[(i,j)] = True
                    count+=1
                    dfs(stack)
                    
        return count
        
        