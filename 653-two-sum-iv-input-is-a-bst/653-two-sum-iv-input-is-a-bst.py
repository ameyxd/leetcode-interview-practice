# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Inorder traversal of BST gives a sorted array
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        sorted_list = []
        self.inorder(root, sorted_list)
        left, right = 0, len(sorted_list) - 1
        while left < right:
            total = sorted_list[left] + sorted_list[right]
            if total > k:
                right -= 1
            elif total < k:
                left += 1
            elif total == k:
                return True
        return False

    def inorder(self, root, inorder_list):
        if root:
            self.inorder(root.left, inorder_list)
            inorder_list.append(root.val)
            self.inorder(root.right, inorder_list)
        
        
        