class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeToEat(k):
            hours = 0 
            for b in piles:
                hours += b//k
                if b%k != 0:
                    hours += 1
            return hours
        l = 1
        high = max(piles)
        while(l<=high):
            mid = (l+high)//2
            if timeToEat(mid) > h:
                l = mid+1
            else:
                high = mid-1 
        return l

        