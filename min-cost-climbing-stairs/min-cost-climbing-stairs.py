class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) 
        dp = [0]*(n+1)
        # def recursive_sol(ind):
        #     if ind<2:
        #         return 0
        #     dp[ind-1] = dp[ind-1] if dp[ind-1] else recursive_sol(ind-1) + cost[ind-1]
        #     dp[ind-2] = dp[ind-2] if dp[ind-2] else recursive_sol(ind-2) + cost[ind-2] 
        #     dp[ind] = min(dp[ind-1] ,dp[ind-2])
        #     return dp[ind]
        # return recursive_sol(len(cost))
        for i in range(n+1):
            if i>=2:
                dp[i] = min(dp[i-1]+ cost[i-1] ,dp[i-2] + cost[i-2]) 
        return dp[n]

                


 