# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r, l = head, head;
        
        while r:
            r = r.next
            if r:
                l = l.next
                r = r.next
        
        return l
        