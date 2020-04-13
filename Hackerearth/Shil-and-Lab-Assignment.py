#/*
#By: Ahmed Moustafa (a.k.a geekahmed)
#Email: geekahmed1@gmail.com
#linkedIn: https://www.linkedin.com/in/geekahmed
#*/

'''
# Sample code to perform I/O:
 
name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT
 
# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
 
# Write your code here
from collections import defaultdict
 
 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def bfs(self, u, matching, visited):
        visited[u] = True
        for v in self.graph[u]:
            uu = matching[v]
            if uu == -1 or not visited[uu] and self.bfs(uu, matching, visited):
                matching[v] = u
                return True
        return False
 
    def maxMatching(self, n):
        matching = [-1] * n
        matches = 0
        for u in range(len(self.graph)):
            if self.bfs(u, matching, [False]*len(self.graph)):
                matches += 1
 
        return matches
 
 
 
n, m = map(int, input().split())
 
a = []
graph = Graph()
for i in range(n):
    a.append(int(input()))
    for j in range(1, min(a[i], m)+1):
        if a[i] % j == 0:
            graph.addEdge(i, j)
 
 
 
print(graph.maxMatching(m+1))
