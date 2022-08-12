# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Decision on whether to pick root or not 0 means don't pick, 1 means pick
        # dp[n, 0] = max(dp[n.left, 1], dp[n.left, 0]) + max(dp[n.right, 1], dp[n.right, 0]
        # dp[n, 1] = dp[n.left, 0] + dp[n.right, 0] + n.val
        
        self.answer = 0
        
        def dp(node): # returns dp(node, 0) and dp(node, 1)
            if not node:
                return (0, 0)
            left, right = dp(node.left), dp(node.right) # Recurse
            bestLeft = max(left[0], left[1]) # best on left btw w/o picking left node and w picking left node
            bestRight = max(right[0], right[1]) # best on right btw w/o picking right node and w picking right node
            wo_picking = bestLeft + bestRight # If you don't pick root, best would be sum of bests in the children
            w_picking = left[0] + right[0] + node.val # if you pick root, you want the w/o picking result of left and right
            self.answer = max(self.answer, wo_picking, w_picking) # best amongst all results for root
            return (wo_picking, w_picking)
        
        dp(root)
        return self.answer