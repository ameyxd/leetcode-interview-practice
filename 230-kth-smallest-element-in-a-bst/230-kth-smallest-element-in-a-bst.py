# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive solution: Get inorder result -> sorted array and return k - 1 th element
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.sorted_elements.append(root.val)
            self.inorder(root.right)
        
    def kthSmallest_1(self, root: Optional[TreeNode], k: int) -> int:
        self.sorted_elements = []
        self.inorder(root)
        print(self.sorted_elements)
        return self.sorted_elements[k - 1]
    
    # Iterative solution
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            curr = node.right
        