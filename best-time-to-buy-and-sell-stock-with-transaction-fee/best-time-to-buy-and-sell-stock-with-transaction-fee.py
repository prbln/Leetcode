class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0]*(2) for _ in range(n+1)]
        # dp[n][0], dp[n][1] = 0,0
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                # print(ind)
                    if buy ==1:
                        profit = max(dp[ind+1][1], -1*prices[ind] + dp[ind+1][0] )
                    else:
                        profit = max(dp[ind+1][0] , prices[ind] + dp[ind+1][1] -fee )
                    dp[ind][buy]= profit
        # print(dp)
        return dp[0][1]