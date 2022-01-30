# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def traverse(root, res):
            if root:
                traverse(root.left, res)
                traverse(root.right, res)
                res.append(root.val)
        traverse(root, res)
        return res