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
q = int(input())
 
for r in range(q):
    S = input()
    T = input()
    charList = [0] * 26
    for char in S:
        charList[ord(char) - ord('a')] += 1
    for char in T:
        charList[ord(char) - ord('a')] -= 1
    print(sum(map(abs, charList)))


