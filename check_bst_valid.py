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
        
        def traverse(node):
            if node == None:
                return []
            left = traverse(node.left)
            right = traverse(node.right)
            return left + [node.val] + right
            
        
        inorder = traverse(root)
        return all(inorder[i] < inorder[i + 1] for i in range(len(inorder) - 1))
        