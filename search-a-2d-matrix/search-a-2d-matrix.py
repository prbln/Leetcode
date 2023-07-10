class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return False
        rowFirstElements = []
        for r in matrix:
            rowFirstElements.append(r[0])
        # print(rowFirstElements)
        def binSearch(high,low, array):
            if high<=low:
                return low
            mid = (high+low)//2
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                return binSearch(mid-1,low,array)
            else: 
                return binSearch(high,mid+1,array)
        rowNum = binSearch(len(rowFirstElements)-1,0, rowFirstElements)
        if target<matrix[rowNum][0]:
            rowNum-=1
        if rowNum<0:
            return False
        ind = binSearch(len(matrix[rowNum])-1,0, matrix[rowNum])
        # print(rowNum,ind)
        if matrix[rowNum][ind] == target:
            return True 
        else:
            return False
