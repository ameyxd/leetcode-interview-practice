# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
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
        