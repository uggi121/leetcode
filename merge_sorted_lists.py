import heapq

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
        
        if not lists:
            return None
        
        h = []
        for node in lists:
            if node:
                heapq.heappush(h, (node.val, node))
        
        result = ListNode(None)
        tail = result
        
        while h:
            pop = heapq.heappop(h)
            node = pop[1]
            next_node = node.next
            if next_node:
                heapq.heappush(h, (next_node.val, next_node))
            node.next = None
            tail.next = node
            tail = tail.next
            
        return result.next