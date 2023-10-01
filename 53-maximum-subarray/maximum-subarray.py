class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0 
        maxSum = -1*float("inf")
        for i in range(len(nums)):
            if curSum>=0:
                curSum+=nums[i]
            else:
                curSum = nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum