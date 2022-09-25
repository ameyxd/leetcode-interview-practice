# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        res = 0
        while queue:
            node = queue.popleft()
            if node:
                if node.left:
                    potLeftLeaf = node.left
                    if not potLeftLeaf.left and not potLeftLeaf.right:
                        res += potLeftLeaf.val
                        
                queue.append(node.left)
                queue.append(node.right)
                
        return res