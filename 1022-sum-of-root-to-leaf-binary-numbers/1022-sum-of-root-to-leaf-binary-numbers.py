# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    # Iterative DFS
    def sumRootToLeaf1(self, root: Optional[TreeNode]) -> int:
        # Time: O(N) Space: O(H)
        stack = [(root, 0)]
        while stack:
            root, n = stack.pop()
            if root:
                n = (n << 1) | root.val
                if not root.left and not root.right:
                    ans += n
                if root.right:
                    stack.append((root.right, n))
                if root.left:
                    stack.append((root.left, n))        
        return ans
    
    # Recursive DFS
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, nums):
            nums = nums * 2 + node.val
            if not node.left and not node.right:
                self.ans += nums
            if node.left:
                dfs(node.left, nums)
            if node.right:
                dfs(node.right, nums)
        dfs(root, 0)
        return self.ans
