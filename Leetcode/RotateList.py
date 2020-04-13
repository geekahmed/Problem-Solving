/*
By: Ahmed Moustafa (a.k.a geekahmed)
Email: geekahmed1@gmail.com
linkedIn: https://www.linkedin.com/in/geekahmed
*/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        size = 0
        start = head
        if k == 0:
            return start
        while head.next is not None:
            head = head.next
            size += 1

        size += 1
        k = k % size
        k = abs(size - k)
        if k == 0:
            return start
        head.next = start

        while k > 0:
            head = head.next
            k -= 1

        start = head.next
        head.next = None
        return start
