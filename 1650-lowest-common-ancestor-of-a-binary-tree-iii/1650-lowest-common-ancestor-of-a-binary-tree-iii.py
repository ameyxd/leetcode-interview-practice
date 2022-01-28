"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        # Make ancestor list of p        
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = p.parent
        
        # Find lowest common ancestor of q in ancestors of p
        while q not in ancestors:
            q = q.parent
        
        return q
            