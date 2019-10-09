# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        def traverse(node):
            if not node:
                return []
            else:
                left = traverse(node.left)
                right = traverse(node.right)
                left.extend(right)
                left.append(node.val)
                return left
        
        return traverse(root)
        