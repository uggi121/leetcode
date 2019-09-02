# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def depth(node):
            if not node:
                return 0
            else:
                if not node.left and node.right:
                    return depth(node.right) + 1
                elif not node.right and node.left:
                    return depth(node.left) + 1
                return min(depth(node.left), depth(node.right)) + 1
        
        return depth(root)
        