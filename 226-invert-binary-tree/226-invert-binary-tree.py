# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
         # Recursive DFS solution
            if not root:
                return None
            
            # Step 1 : Swap children nodes
            tmp = root.left
            root.left = root.right
            root.right = tmp
            
            # Step 2: Invert children subtrees recursively
            self.invertTree(root.left)
            self.invertTree(root.right)
            
            return root