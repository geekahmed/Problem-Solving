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
import sys
sys.setrecursionlimit(1500)
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
 
 
def insert(root, data):
    if not root:
        root = Node(data)
    elif data <= root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root
 
 
def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
 
 
N = int(input())
listIntegers = list(map(int, input().split()))
root = None
for num in listIntegers:
    root = insert(root, num)
 
print(maxDepth(root))
