from collections import defaultdict
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ind = len(nums)
        totalSum = sum(nums)//2
        if sum(nums)%2 !=0:
            return False
        dp = [[0]*(totalSum+1)for _ in range(ind)]
        # if nums[0]
        if nums[0]<=totalSum:
            dp[0][nums[0]] = True 
        else:
            return False
        for i in range(1,ind):
            for j in range(totalSum+1):
                noTake, take = False, False
                if j-nums[i]>=0:
                    val = j-nums[i]
                    take = dp[i-1][val]
                noTake = dp[i-1][j] 
                dp[i][j] = take or  noTake  
            # print(dp,i,j)
        # print(dp) 
        return dp[ind-1][totalSum]           



