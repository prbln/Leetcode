class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r,c = len(obstacleGrid),len(obstacleGrid[0])
        if r==c and r==1:
            if obstacleGrid[0][0] !=1:
                return 1
            return 0
        if obstacleGrid[0][0] ==1:
            return 0 
        dp = [[-1]*c]*r
        dp[0][0] =1 
        for i in range(r):
            for j in range(c):
                up,left = 0,0
                
                if obstacleGrid[i][j] ==1:
                    dp[i][j] = 0 
                else:
                    if i-1>=0:
                        up = dp[i-1][j]
                    if j-1>=0:
                        left = dp[i][j-1]
                    if i==j and i==0:
                        continue
                    dp[i][j] = up+left
            # print(dp)    
        return dp[r-1][c-1]