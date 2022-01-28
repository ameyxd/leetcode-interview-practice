# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Strat: At every point in DFS traversal, if you reach p or q, return it upwards 
        if root in [None, p, q]:
            return root
        
        # Traverse left subtree and then right subtree
        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)
        
        if left_result and right_result: # LCA is root, since p and q exist in either of the two subtrees of root
            return root
        else:
            return left_result or right_result # since result is only returned as non None when node p or node q is found in subtrees of root - use example and propagate value upwards