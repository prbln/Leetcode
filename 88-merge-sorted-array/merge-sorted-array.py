class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m -1
        j = n -1 
        for k in range(m+n-1,-1,-1):
            # print(i,j, nums1, nums2)
            if j<0:
                break
            if i<0:
                nums1[:j+1] = nums2[:j+1]
                break
            nums1[k] = max(nums1[i], nums2[j])
            if nums1[i] > nums2[j]:
                nums1[i] =0 
                i-=1
            else:
                nums2[j] = 0 
                j-=1 
        # print(nums1, nums2, i, j)




        
