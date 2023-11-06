class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 1
        n = len(nums)
        h =  n -2 
        if n==1:
            return nums[0]
        if nums[0]!= nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        while(l<=h):
            mid = (l+h)//2
            print(nums[l], nums[h], mid)
            if nums[mid] == nums[mid+1]:
                if mid %2 ==0:
                    l = mid+1
                else:
                    h = mid-1
            elif nums[mid] == nums[mid-1]:
                if mid %2 ==0:
                    h = mid-1
                else:
                    l = mid+1
            else:
                return nums[mid]
                