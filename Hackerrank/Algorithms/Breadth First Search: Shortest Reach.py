from collections import defaultdict

class Graph:
    def __init__(self, n, edgeWeight):
        self.EDGE_DISTANCE = edgeWeight
        self.visited = [False] * n
        self.distance = [-1]* n
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        queue = list()
        queue.append(start)
        self.visited[start] = True
        self.distance[start] = 0
        while queue:
            u = queue.pop(0)
            for v in self.graph[u]:
                if not self.visited[v]:
                    queue.append(v)
                    self.visited[v] = True
                    self.distance[v] = self.distance[u] + self.EDGE_DISTANCE

        for item in self.distance:
            if item != 0 :
                print(item, end=" ")
        print()



q = int(input())

for Q in range(q):
    noOfNodes, noOfEdges = map(int, input().split())
    graph = Graph(noOfNodes, 6)

    for i in range(noOfEdges):
        u, v = [int(i) for i in input().split(" ")]
        graph.addEdge(u-1, v-1)

    start = int(input())
    graph.bfs(start-1)


