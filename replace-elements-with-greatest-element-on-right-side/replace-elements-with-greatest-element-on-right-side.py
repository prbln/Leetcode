class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ge = -1 
        for i in range(len(arr)-1,-1,-1):
            print(i,ge,arr[i])
            curr = arr[i]
            arr[i] =ge
            if curr> ge:
                ge = curr
        return arr
