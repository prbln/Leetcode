class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount ==0:
            return 1
        n = len(coins)
        dp= [[0]*(amount +1) for _ in range(n)]
        for i in range(amount +1):
            if i%coins[0] ==0:
                dp[0][i] = 1
            else:
                dp[0][i] = 0
        dp[0][0] = 0
        for i in range(1, n):
            for j in range(amount +1):
                if j==0:
                    dp[i][j] = 1
                    continue
                take = 0
                if j-coins[i]>=0:
                    take =  dp[i][j-coins[i]]
                noTake = 0
                noTake = dp[i-1][j]
                dp[i][j] = take+noTake
        return dp[n-1][amount] 