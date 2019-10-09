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
        
        if not head:
            return head
        
        length = 0
        temp = head
        
        while temp:
            temp = temp.next
            length += 1
            
        k = k % length
        
        leader, lagger = head, head
        
        for i in range(k):
            leader = leader.next
        
        while leader.next:
            leader = leader.next
            lagger = lagger.next
        
        leader.next = head
        head = lagger.next
        lagger.next = None
        
        return head
        