/*
By: Ahmed Moustafa (a.k.a geekahmed)
Email: geekahmed1@gmail.com
linkedIn: https://www.linkedin.com/in/geekahmed
*/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = list()
        for item in nums1:
            subArray = nums2[nums2.index(item):]
            nextq = -1
            for i in range(len(subArray)):
                if subArray[i] > item:
                    nextq = subArray[i]
                    break

            res.append(nextq)

        return res

