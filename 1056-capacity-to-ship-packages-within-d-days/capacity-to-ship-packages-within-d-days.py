class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(mid):
            curCargoWt = 0 
            numDays = 0
            for i in range(len(weights)):
                if curCargoWt + weights[i] <= mid:
                    curCargoWt += weights[i]
                else:
                    curCargoWt= weights[i]
                    numDays+=1
            if curCargoWt>0:
                numDays+=1
            return numDays<=days
        l = max(weights)
        h = sum(weights)
        while(l<=h):
            mid = (l+h)//2
            if valid(mid): 
                h = mid -1 
            else:
                l = mid+1
        return l