import math
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # def minStart()
        r,c = len(matrix), len(matrix[0])
        dp = [[-1] * (c) for i in range(r)]
        dp[0] = matrix[0]
        for i in range(1,r):
            for j in range(c):
                upLeft,upright = math.inf,math.inf
                if j-1>=0 : 
                    upLeft = dp[i-1][j-1]
                if j+1<c:
                    upright = dp[i-1][j+1]
                dp[i][j] = matrix[i][j] + min(dp[i-1][j],upLeft,upright)
                # print(dp,dp[i-1][j],upLeft,upright)
        return min(dp[-1])