# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS solution: get max path from left and right subtrees (with no splitting) and check if adding the root makes it larger
        # Return upward the result you will get if you are not allowed to split at that node
        res = [float('-inf')]
        
        # return max path sum without splitting
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0) # if leftmax is negative, you can decide to not select that node, therefore 0
            rightMax = max(rightMax, 0) 
            
            # compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]