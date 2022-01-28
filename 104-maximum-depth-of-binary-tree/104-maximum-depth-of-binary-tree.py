# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
#         # Recursive DFS Solution
#         left_height = 1 + self.maxDepth(root.left)
#         right_height = 1 + self. maxDepth(root.right)
#         return max(left_height, right_height)
    

        # Iterative DFS Solution
        stack = [(root, 1)]
        res = 1
        while stack:
            node, depth = stack.pop()
            if node: # Since I have set this code to include null nodes in stack
                res = max(res, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return res
                