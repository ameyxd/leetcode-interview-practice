# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, node1, node2):
        if not node1 and not node2:
            return True
        if node1 and node2:
            return node1.val == node2.val and self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)
        return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:        
        return self.isMirror(root, root)
    