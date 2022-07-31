# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Time: O(n), bottom up approach
        # recursive function returns height and collectively checks diameter to track max
        # (left height + right height) is the diameter with the current node as root
        self.diameter = 0
        
        def getLongestPath(node):
            if not node:
                return 0
            leftH = getLongestPath(node.left)
            rightH = getLongestPath(node.right)
            
            self.diameter = max(self.diameter, leftH + rightH) # (left height + right height) is the diameter with the current node as root
            
            return max(leftH, rightH) + 1
        
        getLongestPath(root)
        return self.diameter