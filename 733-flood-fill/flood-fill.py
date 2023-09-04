from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        queue.append([sr, sc])
        visited = [[False for j in range(len(image[0]))] for j in range(len(image))]
        def BFS(queue):
            
            while(len(queue)!=0):
                # print(queue)
                r,c = queue.popleft()
                visited[r][c] = True 
                currentColor = image[r][c]
                image[r][c] = color
                adjRow = [-1,0,1,0]
                adjCol = [0,-1,0,1]
                for i in range(4):
                    nxtRow = r + adjRow[i]
                    nxtCol = c + adjCol[i]
                    # print(nxtRow,nxtCol)
                    if nxtRow>=0 and nxtRow<len(image) and nxtCol>=0 and nxtCol<len(image[0]) and image[nxtRow][nxtCol] == currentColor and not visited[nxtRow][nxtCol] :
                        queue.append([nxtRow, nxtCol])
                        visited[nxtRow][nxtCol]= True

        BFS(queue)
        return image
        