class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n ==1 :
            if target == nums[0] or target == -1*nums[0]:
                return 1 
            else:
                return 0      
        ts = sum(nums)
        dp = [[0]*(2*ts + 1) for _ in range(n)]
        if ts < target: 
            return 0
        if -1*ts>target:
            return 0
        mid = ts
        
        dp[0][mid+nums[0]], dp[0][mid-nums[0]] = 1,1
        if mid+nums[0] ==mid-nums[0]:
            dp[0][mid+nums[0]]+=1
        for i in range(1,n):
            for j in range(-1*ts,ts+1):
                takeP,takeN = 0,0
                if j+nums[i]<=ts:
                    takeP = dp[i-1][mid+j+nums[i]]
                if j-nums[i] >=-1*ts:
                    takeN = dp[i-1][mid+(j-nums[i])]
                dp[i][mid+j] = takeP+takeN
        # print(mid,ts)
        return dp[n-1][mid+target]