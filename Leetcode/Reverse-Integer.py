/*
By: Ahmed Moustafa (a.k.a geekahmed)
Email: geekahmed1@gmail.com
linkedIn: https://www.linkedin.com/in/geekahmed
*/

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x>=0 else -1
        temp, x = 0, abs(x)
        while x:
            digit = x%10
            x //= 10
            temp = temp*10 + digit
        temp = temp * sign
        return temp if temp>=-2**31 and temp<=2**31-1 else 0
