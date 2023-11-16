from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        q = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j] ==0:
                    q.append((i,j,0))
                else:
                    mat[i][j] = -1
        while(len(q)!= 0):
            i,j, level = q.popleft()
            nextEle = [[-1,0],[1,0],[0,-1],[0,1]]
            mat[i][j] = level
            for r,c in nextEle:
                nextr = r + i 
                nextc = c + j 
                if min(nextr, nextc) >=0 and nextr<n and nextc<m and mat[nextr][nextc] == -1 and mat[nextr][nextc] != 0 :
                    q.append((nextr, nextc,level+1) )
                    mat[nextr][nextc] = level +1
        return mat

                

            
