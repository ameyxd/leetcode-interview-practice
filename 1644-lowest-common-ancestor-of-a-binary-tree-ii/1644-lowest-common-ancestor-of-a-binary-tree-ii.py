# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        
        parent_dict = {root: None}
        
        while p not in parent_dict or q not in parent_dict:
            if not stack:
                return None
            node = stack.pop()
            if node.left:
                parent_dict[node.left] = node
                stack.append(node.left)
            if node.right:
                parent_dict[node.right] = node
                stack.append(node.right)

        # Make ancestor list of p        
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = parent_dict[p]
        
        # Find lowest common ancestor of q in ancestors of p
        while q not in ancestors:
            q = parent_dict[q]
        
        return q
            