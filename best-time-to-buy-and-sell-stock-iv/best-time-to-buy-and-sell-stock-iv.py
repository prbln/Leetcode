class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0]*(k+1) for _ in range(2)] for _ in range(n+1)]
        # dp[n][0], dp[n][1] = 0,0
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,k+1):
                # print(ind)
                    if buy ==1:
                        profit = max(dp[ind+1][1][cap], -1*prices[ind] + dp[ind+1][0][cap] )
                    else:
                        profit = max(dp[ind+1][0][cap] , prices[ind] + dp[ind+1][1][cap-1] )
                    dp[ind][buy][cap] = profit
        # print(dp)
        return dp[0][1][k]