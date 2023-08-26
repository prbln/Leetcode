class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRow = matrix[0]
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range((m+1)//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][m-j-1]
                matrix[i][m-j-1] = temp
        for i in range(n):
            for j in range(m-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[m-j-1][n-i-1]
                matrix[m-j-1][n-i-1] = temp 