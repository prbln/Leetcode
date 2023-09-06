class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()
        adjList = [[] for i in range(numCourses)]
        visited= [False for i in range(numCourses)]
        indegree= [0 for i in range(numCourses)]
        for i in range(len(prerequisites)):
            a,b =prerequisites[i]
            adjList[b].append(a)
            indegree[a]+=1
        # print(indegree,adjList )
        for i in range(numCourses):
            degree = indegree[i]
            if degree ==0:
                q.append(i)
        topoSort=[]
        def bfs(q):
            while(len(q)!=0):
                print(q)
                ele = q.popleft()
                topoSort.append(ele)
                visited[ele] =True
                for neigh in adjList[ele]:
                    indegree[neigh]-=1
                    if indegree[neigh] ==0 and not visited[neigh]:
                        q.append(neigh)
                        visited[neigh] =True
        bfs(q)
        if len(topoSort) == numCourses :
            return topoSort
        else:
            return []

