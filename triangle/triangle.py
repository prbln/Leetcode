import math
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        r,c = len(triangle),len(triangle[-1])
        dp = [[-1] * (i + 1) for i in range(r)]
        for i in range(0,r):
            for j in range(i+1):
                if i==0 and j ==0:
                    dp[0][0] = triangle[0][0]
                    continue
                up,upRight = math.inf,math.inf
                if j <= i-1:
                    up = dp[i-1][j]
                if j-1>=0: 
                    upRight =  dp[i-1][j-1]
                #     print(up)
                # print(i,j, dp)
                dp[i][j] = min(up,upRight) + triangle[i][j]
            # print()
        return min(dp[r-1])