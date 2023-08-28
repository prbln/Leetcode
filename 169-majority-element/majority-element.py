class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityele = 0
        count =0
        for ele in nums:
            if count ==0:
                majorityele = ele
            if ele == majorityele:
                count+=1
            else:
                count-=1
            
        return majorityele
            
