class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1 
        prev = nums[0]
        count = 1 
        while(i<len(nums)):
            cur = nums[i]
            if cur != prev:
                count+=1
            else:
                nums[i] = 1000
            i+=1
            prev = cur
        nums.sort()
        return count
            
            


