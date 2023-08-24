class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(s):
            area = 0 
            adjrows = [-1,0,1,0]
            adjcols = [0,1,0,-1]
            while(len(s)>0):
                # print(s)
                r,c = s.pop()
                visited[r][c] = True
                area+=1
                for i in range(4):
                    nxtrow = r + adjrows[i]
                    nxtcol = c + adjcols[i]
                    if nxtrow>=0 and nxtrow<n and nxtcol>=0 and nxtcol<m and visited[nxtrow][nxtcol] == False and grid[nxtrow][nxtcol] ==1:
                        visited[nxtrow][nxtcol] = True
                        s.append((nxtrow,nxtcol))
            return area
        #step 01 visted matrix
        n = len(grid)
        m = len(grid[0])
        visited = [[False for j in range(m)] for i in range(n)]
        maxi =0 
        #traversal do dfs whenever you see a one 

        for i in range(n):
            for j in range(m):
                if visited[i][j] ==False and grid[i][j] ==1:
                    s = [(i,j)]
                    maxi = max(maxi, dfs(s))
                visited[i][j] ==True 
        return maxi
