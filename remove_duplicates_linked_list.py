# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        count = defaultdict(int)
        
        head_ptr = head
        
        while head_ptr:
            #print(head_ptr.val)
            count[head_ptr.val] += 1
            head_ptr = head_ptr.next
        
        res = ListNode(None)
        res_ptr = res
        
        head_ptr = head
        
        while head_ptr:
            #print(head_ptr.val, count[head_ptr.val])
            if count[head_ptr.val] == 1:
                res_ptr.next = ListNode(head_ptr.val)
                res_ptr = res_ptr.next
            head_ptr = head_ptr.next
            
        return res.next
                
        