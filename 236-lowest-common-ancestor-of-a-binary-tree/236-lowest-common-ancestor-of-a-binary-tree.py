# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         # Solution: Recursive DFS
#         # Strat: At every point in DFS traversal, if you reach p or q, return it upwards 
#         if root in [None, p, q]:
#             return root
        
#         # Traverse left subtree and then right subtree
#         left_result = self.lowestCommonAncestor(root.left, p, q)
#         right_result = self.lowestCommonAncestor(root.right, p, q)
        
#         if left_result and right_result: # LCA is root, since p and q exist in either of the two subtrees of root
#             return root
#         else:
#             return left_result or right_result # since result is only returned as non None when node p or node q is found in subtrees of root - use example and propagate value upwards
        
        
        # Solution: Iterative with parent pointers
        # Strat: Store the parent pointers to all nodes till you get to p and q inside a dict
        #        Then, you know that where the paths to p and q diverge, that's the LCA of p and q - use example to see paths from root node to p and root node to q
        
        stack = [root]
        
        parent_dict = {root: None}
        
        while p not in parent_dict or q not in parent_dict:
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
            