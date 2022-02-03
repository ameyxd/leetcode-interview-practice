# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recersive solution
    def postorderTraversal_1(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def traverse(root, res):
            if root:
                traverse(root.left, res)
                traverse(root.right, res)
                res.append(root.val)
        traverse(root, res)
        return res
    
    # Recersive solution
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [(root, False)], []
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        return res
                    
