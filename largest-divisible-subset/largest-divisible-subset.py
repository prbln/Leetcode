class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        dp = [1]*n
        hash = [] 
        maxi = 0
        ind_maxi = 0  
        for i in range(n):
            hash.append(i)
        for cur in range(n):
            for prev in range(0, cur):
                if nums[cur] % nums[prev]==0 and dp[cur]< 1+dp[prev]:
                    dp[cur] = 1+dp[prev]
                    hash[cur] = prev 
                    if dp[cur]>maxi:
                        maxi = dp[cur]
                        ind_maxi = cur
        # print(hash,ind_maxi, dp )
        ans = []
        while(hash[ind_maxi]!=ind_maxi ):
            ans.append(nums[ind_maxi])
            ind_maxi = hash[ind_maxi]
        ans.append(nums[ind_maxi])
        return ans[::-1]
