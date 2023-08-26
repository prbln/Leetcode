class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = dict()
        ans = 0 
        for ele in nums:
            check[ele] = True
        for ele in nums:
            if check.get(ele-1, False)== False :
                num = ele
                # print(num)
                while(check.get(num, False)):
                    num+=1
                    
                ans = max(ans, num - ele)
        return ans
                    

