import heapq
import math

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        if len(lists) == 0:
            return None
        if all(sublist == None for sublist in lists):
            return None
        
        h = [(head.val, head) for head in lists if head != None]
        heapq.heapify(h)
        
        result = ListNode(None)
        tail = result
        
        while True:
            if all(i == float('inf') for i, j in h):
                break
            else:
                pair = heapq.heappop(h)
                node, node_n = pair[1], pair[1] 
                node_n = node_n.next
                tail.next = node
                tail = tail.next
                if node_n == None:
                    heapq.heappush(h, (float('inf'), node_n))
                else:
                    heapq.heappush(h, (node_n.val, node_n))
        
        return result.next
            