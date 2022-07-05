# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def check(self, root, leftMax, rightMin):
        if not root:
            return True
        leftRes = self.check(root.left, leftMax, root.val)
        rightRes = self.check(root.right, root.val, rightMin)
        valCheck = (leftMax < root.val < rightMin)
        
        return leftRes and rightRes and valCheck
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # check if root is greater than left subtree nodes and less than right subtree nodes
        # keep track of max value in left subtree and min val in right subtree

        return self.check(root, float("-inf"), float("inf"))
        