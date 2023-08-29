class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        i = 0 
        j = len(nums)-1
        p = i+1
        q = j-1
        ans = []
        while(i<len(nums)):
            while(i<j):
                while(p<q):
                    summ = nums[i] + nums[j] + nums[p] + nums[q]
                    if summ ==target:
                        ans.append([nums[i] ,  nums[p] , nums[q], nums[j]] )
                        prevP = p 
                        while(nums[prevP]==nums[p] and p<q ):
                            p+=1
                    elif summ<target:
                        p+=1 
                    else:
                        q-=1 
                prevJ = j 
                while(nums[prevJ]==nums[j] and j > i):
                    j-=1
                p = i+1 
                q = j-1
            prevI = i 
            while(i<len(nums) and nums[prevI]==nums[i]):
                i+=1
            j = len(nums)-1
            p = i+1
            q = j-1
        return ans 
            