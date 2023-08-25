class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0 
        maxi = -1
        for i in range(n-1,-1,-1):
            maxi = max(maxi, prices[i])
            ans = max(ans,maxi - prices[i] )
        return ans
