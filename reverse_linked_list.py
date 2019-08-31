# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        p1 = head
        p2 = None
        if p1 != None:
            p2 = head.next
        
        while p2 != None:
            #print("P2: ", p2.val)
            p1.next = p2.next 
            p2.next = head
            head = p2
            #print("HEAD: ", head.val)

            p2 = p1.next
        
        return head