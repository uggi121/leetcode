# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        ptr = head
        
        if not ptr:
            return ptr
        
        while ptr and ptr.next:
            if ptr.next.val == ptr.val:
                ptr.next = ptr.next.next
            else:    
                ptr = ptr.next
        
        return head
        