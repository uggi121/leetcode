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
        
        if not root:
            return []
        
        stack = []
        stack.append(root)
        
        result = []
        left = set()
        right = set()
        
        while stack:
            node = stack.pop()
            if node.left and node.left not in left:
                stack.append(node.left)
                stack.append(node)
                left.add(node.left)
            elif node.right and node.right not in right:
                stack.append(node.right)
                stack.append(node)
                right.add(node.right)
            else:
                result.append(node.val)
        
        return result[::-1]