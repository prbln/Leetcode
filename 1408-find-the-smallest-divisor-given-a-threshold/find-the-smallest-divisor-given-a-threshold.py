import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def valid(mid):
            summ = 0 
            for i in range(len(nums)):
                summ+=math.ceil(nums[i]/mid)
            return summ<=threshold
        l = 1 
        h = max(nums)
        ans = 0 
        while(l<=h):
            mid = (l+h)//2
            if valid(mid):
                ans = mid
                h = mid-1
            else:
                l = mid+1
        return ans