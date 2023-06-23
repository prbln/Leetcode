import math
class Solution:
    count = 0 
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp= [[math.inf]*(amount +1) for _ in range(n)]
        for i in range(amount +1):
            if i%coins[0] ==0:
                dp[0][i] = i//coins[0]
            else:
                dp[0][i] = math.inf
        dp[0][0] = 0
        for i in range(0, n):
            for j in range(amount +1):
                if j==0:
                    dp[i][j] = 0
                    continue
                take = math.inf
                if j-coins[i]>=0:
                    take = 1 + dp[i][j-coins[i]]
                noTake = -1
                noTake = dp[i-1][j]
                dp[i][j] = min(take,noTake)
        if dp[n-1][amount]  == math.inf:
            return -1
        else:
            return dp[n-1][amount]   
        
        

            