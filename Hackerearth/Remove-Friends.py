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
def removeFriend(k, friends):
    temp = []
    for friend in friends:
        while k and temp and temp[-1] < friend:
            temp.pop()
            k -= 1
        temp.append(friend)
    print(" ".join(map(str,temp)))
 
 
q = int(input())
for i in range(q):
    N, K = map(int, input().split())
    friends = map(int, input().split())
    removeFriend(K, friends)
