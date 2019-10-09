# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def helper(node, lower, upper):
            if not node:
                return True
            else:
                return (helper(node.left, lower, node.val)
                        and lower < node.val and node.val < upper
                        and helper(node.right, node.val, upper))
        
        return helper(root, float('-inf'), float('inf'))
                
            
        