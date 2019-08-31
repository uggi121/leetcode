# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1, p2 = head, head
        
        if head == None:
            return False
        
        while True:
            p2 = p2.next
            if p2 == None:
                return False
            elif p1 is p2:
                return True
            p2 = p2.next
            if p2 == None:
                return False
            p1 = p1.next
            if p1 is p2:
                return True