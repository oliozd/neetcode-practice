# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS(recursive)
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        """
        #BFS(Iterative) - Queue
        """
        if not root:
            return 0
        q = deque([root])
        level = 0
        while q:
            for i in range(len(q)): # iterate through level
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        
        return level
        """
        #DFS(Iterative)- Stack

        if not root:
            return 0
        
        stack = [[root, 1]]
        max_depth = 0 
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth) # Track max depth
            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
        
        return max_depth
            



        

        

        