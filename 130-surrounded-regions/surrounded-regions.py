class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        visited = dict()
        stack = []
        def dfs(stack):
            print(stack)
            while(len(stack) != 0 ):
                i, j = stack.pop()
                visited[(i,j)] = True
                nextEle = [[-1,0],[1,0],[0,-1],[0,1]]
                for r,c in nextEle:
                    nextR = i + r
                    nextC = j + c
                    if nextR < n and nextC < m and min(nextR, nextC)>=0 and not visited.get((nextR, nextC), False) and board[nextR][nextC] == "O":
                        stack.append((nextR, nextC)) 
                        visited[(nextR, nextC)] = True
        for i in [0,n-1]:
            for j in range(m):
                if board[i][j] == "O":
                    stack.append((i,j))
                    dfs(stack)
        for i in range(n):
            for j in [0,m-1]:
                if board[i][j] == "O":
                    stack.append((i,j))
                    dfs(stack)
        for i in range(n):
            for j in range(m):
                if not visited.get((i,j), False) and board[i][j] == "O" and i:
                    board[i][j] = "X"
        return board