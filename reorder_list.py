import Queue

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        q = Queue.Queue()
        stack = []
        fast, middle = head, head
        
        if not head:
            return None
        
        while fast.next:
            fast = fast.next
            if not fast.next:
                break
            fast = fast.next
            middle = middle.next
        
        ptr = head
        while ptr != middle:
            node = ptr
            ptr = ptr.next
            node.next = None
            q.put(node)
        
        node = ptr
        ptr = ptr.next
        node.next = None
        q.put(node)
        
        
        while ptr:
            node = ptr
            ptr = ptr.next
            node.next = None
            stack.append(node)
            
        result = ListNode(None)
        tail = result
        
        #print(q, stack)
        while not q.empty() or len(stack) != 0:
            node1 = q.get()
            #print(node1)
            tail.next = node1
            if q.empty() and len(stack) == 0:
                break
            tail = tail.next
            node2 = stack.pop()
            tail.next = node2
            #print(node2)
            tail = tail.next
        
        return result.next
        
            