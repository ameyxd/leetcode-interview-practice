# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Strat: LCA will be either where the split occurred, i.e., p is on left of node and q is on right of node, or if we reach p or q, i.e., p is ancestor to itself and q or q is ancestor it p or itself
        curr = root
        while True:    # Essentiallty we want to keep going until we guaranteed return
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else: # We have got curr to the point where p < curr < q or if curr == p or if curr == q
                return curr
        
                