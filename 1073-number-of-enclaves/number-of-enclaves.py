class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = dict()
        def dfs(stack):
            setcountZero = False
            count = 0 
            while(len(stack)!= 0):
                i,j = stack.pop()
                visited[(i,j)] = True
                # print(i,j)
                if i == 0 or i == n-1 or j == m-1 or j ==0:
                    setcountZero = True  
                count+=1
                nextEle = [[0,1],[0,-1],[1,0],[-1,0]]
                for r,c in nextEle:
                    nextr = i+r
                    nextc = j+c
                    
                    if min(nextr,nextc) >=0 and  nextr<n and nextc<m and grid[nextr][nextc] == 1 and not visited.get((nextr,nextc), False):
                        if (nextr == n-1 or nextc==m-1 or nextr ==0 or nextc ==0): 
                            setcountZero = True  
                        stack.append((nextr, nextc))
                        visited[(nextr, nextc)] = True
            if setcountZero:
                return 0 
            return count 
        TotalCount = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited.get((i,j), False):
                    count = dfs([(i,j)])
                    # print(count, "count")
                    if count:
                        TotalCount +=count
        return TotalCount


                    