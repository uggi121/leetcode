# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        p1, p2 = head, head
        for i in range(n):
            p2 = p2.next
        
        if p2 == None:
            head = head.next
            return head
        
        while p2.next != None:
            p2 = p2.next
            p1 = p1.next
        
        p1.next = p1.next.next
        
        return head
            