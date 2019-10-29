# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:38:54 2019

@author: Sudharshan
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        length, length_ptr = 0, head
    
        while length_ptr:
            length += 1
            length_ptr = length_ptr.next

        dummy_node = start = ListNode(None)
        dummy_node.next = start.next = head

        for i in range(length // k):
            prev, cur = start.next, start.next.next
            for j in range(k - 1):
                temp = cur.next
                cur.next = prev
                prev, cur = cur, temp
            start.next.next, tmp = cur, start.next
            start.next = prev
            start = tmp

        return dummy_node.next
