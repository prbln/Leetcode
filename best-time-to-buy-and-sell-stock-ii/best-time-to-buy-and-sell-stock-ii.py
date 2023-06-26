class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*(2) for _ in range(n+1)]
        dp[n][0], dp[n][1] = 0,0
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                # print(ind)
                if buy ==0:
                    profit = max(dp[ind+1][0], -1*prices[ind] + dp[ind+1][1])
                else:
                    profit = max(dp[ind+1][1], prices[ind] + dp[ind+1][0])
                dp[ind][buy] = profit
        # print(dp)
        return dp[0][0]
