# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        if not root:
            return 0
        
        def inorder(node):
            if not node:
                return []
            else:
                left = inorder(node.left)
                left.append(node.val)
                left.extend(inorder(node.right))
                return left
        
        return inorder(root)[k - 1]
            
        