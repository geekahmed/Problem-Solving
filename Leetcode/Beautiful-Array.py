/*
By: Ahmed Moustafa (a.k.a geekahmed)
Email: geekahmed1@gmail.com
linkedIn: https://www.linkedin.com/in/geekahmed
*/

class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        res = []
        if N==1:
            res.append(1)
            return res
    
        else:
            odd = self.beautifulArray((N+1)/2)
            for i in range(len(odd)):
                res.append(2*odd[i] - 1)
            
            even = self.beautifulArray(N/2)
            for i in range(len(even)):
                res.append(2*even[i])


        return res

