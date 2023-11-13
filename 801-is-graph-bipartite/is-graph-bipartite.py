class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = dict()

        def DFS(stack):
            while(len(stack)>0):
                node, color = stack.pop()
                green = True if  color == "green" else False 
                visited[node] = color
                for neighbor in graph[node]:
                    if visited.get(neighbor, False):
                        if visited[neighbor] == color:
                            return False
                    else:
                        stack.append((neighbor, "yellow" if  color == "green" else  "green" ))
                        visited[neighbor] = "yellow" if  color == "green" else  "green"
            return True
        for i in range(n):
            stack = []
            if not visited.get(i, False):
                stack.append((i, "green"))
                visited[i] = "green"
                if not DFS(stack) :
                    return False
        return True

        