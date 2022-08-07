# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        
        def helper(root, high, low):
            if root:
                if root.val >= low and root.val <= high:
                    self.total += root.val
                helper(root.left, high, low)
                helper(root.right, high, low)
        helper(root, high, low)
        return self.total