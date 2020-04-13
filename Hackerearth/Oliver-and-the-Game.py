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
import sys
sys.setrecursionlimit(10000)
 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = [False] * 100001
        self.inTime = [0] * 100001
        self.outTime = [0] * 100001
        self.timer = 0
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def DFS(self, v):
        self.visited[v] = True
        self.timer += 1
        self.inTime[v] = self.timer
        for u in self.graph[v]:
            if not self.visited[u]:
                self.DFS(u)
        self.timer += 1
        self.outTime[v] = self.timer
 
    def query(self, u, v):
        return ((self.inTime[u] < self.inTime[v] and self.outTime[u] > self.outTime[v]) or (
                    self.inTime[v] < self.inTime[u] and self.outTime[v] > self.outTime[u]))
 
    def isParent(self, u, v):
        if self.inTime[u] < self.inTime[v] and self.outTime[u] > self.outTime[v]:
            return True
        return False
 
 
 
n = int(input())
graph = Graph()
for _ in range(n-1):
    u, v = map(int, input().split())
    graph.addEdge(u, v)
 
graph.DFS(1)
 
q = int(input())
 
for Q in range(q):
    d, x, y = map(int, input().split())
    if not graph.query(x, y):
        print("NO")
    else:
        if d:
            if graph.isParent(x,y):
                print("NO")
            else:
                print("YES")
        else:
            if graph.isParent(x, y):
                print("YES")
            else:
                print("NO")



