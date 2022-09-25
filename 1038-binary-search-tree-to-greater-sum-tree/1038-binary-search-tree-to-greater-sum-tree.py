# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # reverse inorder traversal
        stack = []
        curr = root
        currSum = 0
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()
            currSum += curr.val
            curr.val = currSum
            curr = curr.left
        return root