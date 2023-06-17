class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dictt = {}

        def checkTarget(ind, summ, count):
            # print(summ)
            if target == summ and ind == n:
                count+=1
                return count
            if ind>=n :
                return count 
            if (ind,summ) in dictt:
                return dictt[(ind,summ) ]
            else:
                take_positive = checkTarget(ind+1, summ  + nums[ind], count) 
                take_negative = checkTarget(ind+1, summ - nums[ind], count)
                dictt[(ind,summ)] = take_positive + take_negative
            # print(take_positive,take_negative )
            return dictt[(ind,summ)]
        return checkTarget(0,0, 0)
