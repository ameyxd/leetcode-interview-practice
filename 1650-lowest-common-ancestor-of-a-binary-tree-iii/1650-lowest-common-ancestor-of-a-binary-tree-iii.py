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
#         stack = [root]
        
#         parent_dict = {root: None}
        
#         while p not in parent_dict or q not in parent_dict:
#             if not stack:
#                 return None
#             node = stack.pop()
#             if node.left:
#                 parent_dict[node.left] = node
#                 stack.append(node.left)
#             if node.right:
#                 parent_dict[node.right] = node
#                 stack.append(node.right)

        # Make ancestor list of p        
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = p.parent
        
        # Find lowest common ancestor of q in ancestors of p
        while q not in ancestors:
            q = q.parent
        
        return q
            