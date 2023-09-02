class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        rigthMax = []
        rigthMaxEle = -1
        for ele in height:
            rigthMax.append(rigthMaxEle)
            if ele >=rigthMaxEle:
                rigthMaxEle = ele
            

        leftMax = []
        leftMaxEle = -1
        for i in range(len(height)-1, -1, -1):
            ele = height[i]
            leftMax.append(leftMaxEle) 
            if ele >leftMaxEle:
                leftMaxEle = ele
        # print(leftMax,rigthMax)
        n = len(height)
        for i in range(n):
            waterTrapped = min(leftMax[n-i-1],rigthMax[i]) - height[i] 
            if waterTrapped>0:
                ans += waterTrapped
        return ans

            