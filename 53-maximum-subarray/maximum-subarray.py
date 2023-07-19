class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        currSum = 0 
        maxSum = -1*math.inf
        for ele in nums:
            if currSum+ele<0:
               maxSum = max(maxSum,currSum,ele)
               currSum = max(ele,0)
            else:
                currSum+=ele
                if currSum> maxSum:
                    maxSum = currSum
        return maxSum 