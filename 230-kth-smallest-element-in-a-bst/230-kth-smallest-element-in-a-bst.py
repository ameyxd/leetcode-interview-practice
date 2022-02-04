# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.sorted_elements.append(root.val)
            self.inorder(root.right)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.sorted_elements = []
        self.inorder(root)
        print(self.sorted_elements)
        return self.sorted_elements[k - 1]