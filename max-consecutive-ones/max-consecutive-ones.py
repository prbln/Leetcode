class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxiOverall = 0
        curCount = 0 
        for i in range(len(nums)):
            if nums[i] ==1:
                curCount+=1 
            else:
                maxiOverall = max(maxiOverall,curCount )
                curCount = 0
        return max(maxiOverall,curCount )
