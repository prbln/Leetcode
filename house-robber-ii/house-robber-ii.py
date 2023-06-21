class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        def funct(num1):
            # print(num1)
            n= len(num1)
            if n<1:
                return 0
            if n ==1:
                return num1[0]
            dp= [0]*(n)
            dp[0] = num1[0]
            dp[1] = max(num1[0],num1[1])
            for i in range(2,n):
                dp[i] = max(dp[i-2] + num1[i] , dp[i-1])
            return dp[n-1]
        return max(funct(nums[0:-1]), funct(nums[1:]))

        