class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.append(1)
        nums.insert(0,1)
        print(nums)
        n = len(nums)
        dp = [[0]*(n) for _ in range(n)]
        
        for i in range(n-2,0,-1):
            for j in range(1,n-1):
                
                if i<=j:
                    for ind in range(i,j+1):
                        # print(i,j)
                        dp[i][j] = max(dp[i][j],(nums[i-1] * nums[ind] * nums[j+1]) + dp[i][ind-1] + dp[ind+1][j])
        # print(dp)
        return dp[1][n-2]



