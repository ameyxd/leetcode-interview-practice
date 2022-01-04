# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # SOLUTION 1: Check if list from inorder traversal is sorted or not
    def isValidBST_1(self, root: Optional[TreeNode]) -> bool:
        result = []
        self.inorderCheck(root, result)
        for i in range(len(result)-1):
            if result[i+1] <= result[i]:
                return False
        return True
        
    def inorderCheck(self, root, inorder_list):
        if root:
            self.inorderCheck(root.left, inorder_list)
            inorder_list.append(root.val)
            self.inorderCheck(root.right, inorder_list)
        
    # SOLUTION 1: Check if root vals are greater than all vals in left subtree and less than all vals in right subtree
    def check(self, root, leftMax, rightMin):
        if not root:
            return True
        l = self.check(root.left, leftMax, root.val)
        v = (leftMax < root.val < rightMin)
        r = self.check(root.right, root.val, rightMin)
        return l and v and r

    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, float("-inf"), float("inf"))
        

