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
n, k = map(int, input().split())
 
a = list(map(int, input().split()))
 
a.sort()
 
left = 0
right = n - 1
flag = False
while left < right:
    if a[left] + a[right] == k:
        print("YES")
        flag = True
        break
    elif a[left] + a[right] > k:
        right -= 1
    else:
        left += 1
 
if not flag:
    print("NO")
