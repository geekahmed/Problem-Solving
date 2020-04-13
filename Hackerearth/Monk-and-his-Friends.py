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
t = int(input())
for k in range(t):
    N, M = map(int, input().split())
 
    listOfIntegers = list(map(int, input().split()))
    givenList = {}
 
    for i in range(N):
        givenList[listOfIntegers[i]] = True
    for i in range(N, len(listOfIntegers)):
        if listOfIntegers[i] in givenList:
            print("YES")
        else:
            print("NO")
            givenList[listOfIntegers[i]] = True
