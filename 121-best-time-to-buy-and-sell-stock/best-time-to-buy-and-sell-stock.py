class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp =[]
        maxi = -1 
        revLsit = prices[::-1]
        for i in range(len(prices)):
            maxi = max(maxi,revLsit[i]) 
            temp.append(maxi)
        greatestValAfterMe = temp[::-1]
        print(greatestValAfterMe)
        ans = 0 
        for i in range(len(prices)):
            ans = max(ans, greatestValAfterMe[i] - prices[i])
        return ans