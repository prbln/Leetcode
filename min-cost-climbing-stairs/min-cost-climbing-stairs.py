class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        def recursive_sol(ind):
            if ind<2:
                return 0
            dp[ind-1] = dp[ind-1] if dp[ind-1] else recursive_sol(ind-1) + cost[ind-1]
            dp[ind-2] = dp[ind-2] if dp[ind-2] else recursive_sol(ind-2) + cost[ind-2] 
            dp[ind] = min(dp[ind-1] ,dp[ind-2])
            return dp[ind]
        return recursive_sol(len(cost))
