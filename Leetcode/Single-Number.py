/*
By: Ahmed Moustafa (a.k.a geekahmed)
Email: geekahmed1@gmail.com
linkedIn: https://www.linkedin.com/in/geekahmed
*/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        HASH = dict()
        for i in nums:
            try:
                HASH.pop(i)
            except:
                HASH[i] = 1
        return HASH.popitem()[0]

