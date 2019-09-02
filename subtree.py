# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        def traverse(s, t):
            if not t:
                return True
            elif not s:
                return False
            else:
                return traverse(s.left, t) or traverse(s.right, t) or equals(s, t)
        
        def equals(s, t):
            if not t and not s:
                return True
            elif not t:
                return False
            elif not s:
                return False
            else:
                return (s.val == t.val 
                            and equals(s.left, t.left) 
                            and equals(s.right, t.right))
        return traverse(s, t)