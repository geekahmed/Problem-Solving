/*
By: Ahmed Moustafa (a.k.a geekahmed)
Email: geekahmed1@gmail.com
linkedIn: https://www.linkedin.com/in/geekahmed
*/

class Solution(object):
    def reverseString(self, s):
        start = 0
        end = len(s) - 1 
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
