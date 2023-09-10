class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextgreaterEle = dict()
        stack = []
        ans = []
        for i in range(len(nums2)):
            ele = nums2[i]
            while(len(stack) >0 and stack[-1]<ele):
                nextgreaterEle[stack.pop()]  = ele
            stack.append(ele)
        while(len(stack)) >0:
            nextgreaterEle[stack.pop()] = -1 
        # print(nextgreaterEle)
        for ele in nums1:
            ans.append(nextgreaterEle[ele])
        return ans 
            

