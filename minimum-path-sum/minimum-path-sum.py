import math
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c = len(grid), len(grid[0])
        dp = [[-1]*c]*r
        dp[0][0] = grid[0][0]
        for i in range(r):
            for j in range(c):
                
                if i==j and i ==0:
                    continue
                up,left = math.inf, math.inf
                if i-1>=0:
                    up = dp[i-1][j]
                if j-1>=0:
                    left = dp[i][j-1]
                dp[i][j] = grid[i][j]  + min(up,left)
        return dp[r-1][c-1]