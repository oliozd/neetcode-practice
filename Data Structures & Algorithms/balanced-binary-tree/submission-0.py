# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        isbalanced = True
        def recurse(node):
            
            nonlocal isbalanced
            if not node:
                return 0
            
            lh = recurse(node.left)
            rh = recurse(node.right)
            
            result = abs(lh - rh)
                
            if result > 1:
                isbalanced = False
            
            return 1 + max(lh, rh)
        
        recurse(root)

        return isbalanced

            


