from collections import defaultdict
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ%2 != 0:
            return False
        target = summ//2
        dp = [[False]*(target+1) for _ in range(len(nums))]
        # def targetcheck(ind,target):
        #     if ind>=len(nums):
        #         return False
        #     if target ==0:
        #         return True
        #     ele = nums[ind]
        #     dp[ind+1][target]  = dp[ind+1][target] if dp[ind+1][target]  else targetcheck(ind+1, target )
             
        #     dp[ind+1][target-ele]  =  dp[ind+1][target-ele]  if dp[ind+1][target-ele] else targetcheck(ind+1, target-ele )
        #     return dp[ind+1][target] or dp[ind+1][target-ele]

        # return targetcheck(0,target)
        for i in range(len(nums)):
            dp[i][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1,len(nums)):
            for j in range(1,target+1):
                if j>=nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        # print(len(nums)-1,target)
        # print(dp)
        return dp[len(nums)-1][target]
