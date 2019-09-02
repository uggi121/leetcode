# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder.pop(0))
        idx = inorder.index(root.val)
        left = inorder[:idx]
        right = inorder[idx + 1:]
        root.left = self.buildTree(preorder, left)
        root.right = self.buildTree(preorder, right)
        return root
        