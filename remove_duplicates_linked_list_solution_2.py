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
        
        head_duplicate = False
        while head and head.next and head.next.val == head.val:
            head = head.next
            head_duplicate = True
        
        leader, lagger = head, ListNode(None)
        lagger.next = head
        
        while leader:
            can_delete = False
            while leader.next and leader.next.val == leader.val:
                can_delete = True
                leader = leader.next
            leader = leader.next
            if can_delete:
                while lagger.next and not lagger.next is leader: 
                    lagger.next = lagger.next.next
            else:
                lagger = lagger.next
        
        return head if not head_duplicate else head.next
                
        