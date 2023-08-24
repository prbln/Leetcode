class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(s):
            # print("yo")
            
            while(len(s)>0):
                # print(visited, s)
                r,c = s.pop()
                visited[r][c] = True 
                adjRows = [-1,0,1,0]
                adjcol = [0,1,0,-1]

                for i in range(4):
                    nextrow = r + adjRows[i]
                    nextcol = c + adjcol[i]
                    if nextrow >= 0 and nextrow<n and nextcol>=0 and nextcol<m and grid[nextrow][nextcol] =="1" and visited[nextrow][nextcol] ==False  :
                        s.append((nextrow,nextcol))
            

        n = len(grid)
        m = len(grid[0])
        visited = [[ False for j in range(m)] for i in range(n)]
        # print(n,m, len(visited), len(visited[0]))
        count = 0 
        for i in range(n):
            for j in range(m):
                # print
                if visited[i][j] == False and grid[i][j] =="1":
                    # print(i,j)
                    stack = [(i,j)]
                    dfs(stack)
                    count+=1
                visited[i][j] = True
        
        return count  
                
                