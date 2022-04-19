# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth_1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack, min_depth = [(1, root)], float('inf')

        while stack:
            depth, root = stack.pop()
            
            children = [root.left, root.right]
            
            if not any(children): #leaf node
                min_depth = min(min_depth, depth)
            
            for node in children:
                if node:
                    stack.append((depth + 1, node))
        
        return min_depth