# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node, path):
            if node:
                path += str(node.val)
                if not node.right and not node.left:
                    res.append(path)
                else:
                    path += '->'
                    dfs(node.left, path)
                    dfs(node.right, path)            
        dfs(root, "")
        return res
    
    # DFS Iterative Stack
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
            if not node.right and not node.left: # reached leaf node
                res.append(path)
                
        return res