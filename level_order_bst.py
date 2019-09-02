from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level_order = [[]]
        
        if not root:
            return []
        
        def neighbors(node):
            if node:
                return (node.left, node.right)
            return None
        
        q = deque()
        
        q.append((root, 0))
        
        while q:
            level_order.append([])
            v = q.popleft()
            level_order[v[1]].append(v[0].val)
            for nbr in neighbors(v[0]):
                if nbr:
                    q.append((nbr, v[1] + 1))
        
        return [sublist for sublist in level_order if sublist]
            