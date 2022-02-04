# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, sorted_elements):
        if root:
            self.inorder(root.left, sorted_elements)
            sorted_elements.append(root.val)
            self.inorder(root.right, sorted_elements)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_elements = []
        self.inorder(root, sorted_elements)
        print(sorted_elements)
        return sorted_elements[k - 1]