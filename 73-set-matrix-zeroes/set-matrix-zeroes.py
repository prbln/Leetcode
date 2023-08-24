class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = dict()
        col = dict()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] ==0:
                    row[r] = row.get(r, True)
                    col[c] = col.get(c,True)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if row.get(r,False) or col.get(c,False):
                    matrix[r][c] = 0 
        return matrix

                

