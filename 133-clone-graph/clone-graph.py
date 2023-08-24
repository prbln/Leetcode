class Solution:
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        # print(node.val,node.neighbors,Solution.visited)
        if node.val in self.visited:
            return self.visited[node.val]
        new_node = Node(node.val)
        self.visited[node.val] = new_node
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(neighbor))
        return new_node
