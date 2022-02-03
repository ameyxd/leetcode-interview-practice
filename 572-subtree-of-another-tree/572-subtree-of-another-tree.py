# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive solution using the isSameTree logic
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right))
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Subroot doesn't exist - it is a subtree of root
        if not subRoot:
            return True
        if not root:
            return False
        # Tree starting at root is same as subRoot
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)