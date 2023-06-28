from collections import defaultdict 
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        maxi = 0
        ans  = [1]*n
        for curInd in range(n):
            for prevInd in range(curInd):
                if nums[prevInd] < nums[curInd] and dp[curInd] == 1 + dp[prevInd]:
                    ans[curInd]+= ans[prevInd]
                if nums[prevInd] < nums[curInd] and dp[curInd] < 1+ dp[prevInd]:
                    dp[curInd] = dp[prevInd] + 1
                    ans[curInd]= ans[prevInd]
        x = max(dp)
        # print(dp,x, ans)
        sol = 0 
        for i in range(n):
            if dp[i] ==x:
                sol +=ans[i]
        return sol
