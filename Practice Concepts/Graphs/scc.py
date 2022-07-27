# Python implementation to find Strongly Connected Components

from collections import defaultdict

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)
    
    # Add edge to the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)
    
    # DFS
    def dfs(self, d, visitedVertex):
        visitedVertex[d] = True
        print(d, end=' ')
        for i in self.graph[d]:
            if not visitedVertex[i]:
                self.dfs(i, visitedVertex)

    def fill_order(self, d, visitedVertex, stack):
        visitedVertex[d] = True
        for i in self.graph[d]:
            if not visitedVertex[i]:
                self.fill_order(i, visitedVertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # Print stongly connected components
    def print_scc(self):
        stack = []
        visitedVertex = [False] * (self.V)

        for i in range(self.V):
            if not visitedVertex[i]:
                self.fill_order(i, visitedVertex, stack)

        gr = self.transpose()

        visitedVertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visitedVertex[i]:
                gr.dfs(i, visitedVertex)
                print("")


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_scc()