# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append(root.val)
            self.inorder(root.right, result)
        
    
    def inorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorder(root, result)
        return result
    
    # Iterative
    def inorderTraversal_1(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                popped = stack.pop()
                result.append(popped.val)
                root = popped.right
        return result
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [(root, False)], []
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                res.append(node.val)
            else:
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
        return res

                
        
    