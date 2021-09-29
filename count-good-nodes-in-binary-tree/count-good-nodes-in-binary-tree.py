# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        
        def traverse(node, max_so_far):
            nonlocal num_good_nodes
            
            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.right:
                traverse(node.right, max(node.val, max_so_far))
            if node.left:
                traverse(node.left, max(node.val, max_so_far))

        
        num_good_nodes = 0
        traverse(root, float("-inf"))
        return num_good_nodes