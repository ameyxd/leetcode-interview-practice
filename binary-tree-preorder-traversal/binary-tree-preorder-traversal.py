# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            
        # Recursive solution
        def traverse(node, preorder_res):
            if not node:
                return
            preorder_res.append(node.val)
            traverse(node.left, preorder_res)
            traverse(node.right, preorder_res)

        preorder_res = []
        traverse(root, preorder_res)
        return preorder_res
    
    
        # Iterative solution using stack
#         if not root:
#             return []
#         preorder_res, stack = [], [root]
        
#         while stack:
#             node = stack.pop()
#             preorder_res.append(node.val)
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#         return preorder_res
