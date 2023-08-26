class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        minRow = 0 
        maxRow = len(matrix)-1
        minCol = 0 
        maxCol = len(matrix[0])-1
        ans = []
        while(minRow<=maxRow and minCol<=maxCol):
            col = minCol 
            
            while(col<=maxCol ):
                ans.append(matrix[minRow][col])
                col+=1
            minRow+=1
            row= minRow
            while(row<=maxRow ):
                ans.append(matrix[row][maxCol])
                row+=1
            maxCol-=1
            col = maxCol
            # print(col,minCol)
            while(col>=minCol and minRow<=maxRow ):
                ans.append(matrix[maxRow][col])
                col-=1
            maxRow -=1
            row = maxRow
            while(row>=minRow and minCol<=maxCol):
                ans.append(matrix[row][minCol])
                row-=1
            minCol+=1 
        return ans


