# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(nlogn) (at every point, height will be called logn times)
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
    # Top down approach
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Base case: No node = balanced
        if not root:
            return True
        # Condition for imbalance based on height
        if (abs(self.height(root.left) - self.height(root.right)) > 1):
            return False
        # Balanced only if right and left side are balanced
        return self.isBalanced(root.left) and self.isBalanced(root.right)