# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:41:37 2019

@author: Sudharshan
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        dummy_node = start = ListNode(None)
        dummy_node.next = start.next = head
        
        for i in range(0, m - 1):
            start = start.next
            
        prev, cur = start.next, start.next.next
        
        for i in range(m, n):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
            
        start.next.next = cur
        start.next = prev
        
        return dummy_node.next