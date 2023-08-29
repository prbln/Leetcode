class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#step 01 sort 
        nums.sort()
        i = 0 
        ans =[]
        j = 1
        k = len(nums)-1
        while(i<j<k):
            # print(i,j,k)
            while(j<k):
                summ = nums[i] + nums[j] + nums[k]
                if summ ==0:
                    prevJ = j 
                    prevK = k
                    while(nums[prevJ]==nums[j] and j<k):
                        j+=1 
                    while(nums[prevK]==nums[k] and k>j):
                        k-=1
                    ans.append([nums[i],nums[prevJ],nums[prevK]])
                elif summ<0:
                    j+=1 
                else :
                    k-=1 
                # print(i,j,k)
            prevI=i
            while(i<len(nums) and nums[prevI]==nums[i]  ):
                i+=1 
            j = i+1 
            k = len(nums)-1

        return ans

            