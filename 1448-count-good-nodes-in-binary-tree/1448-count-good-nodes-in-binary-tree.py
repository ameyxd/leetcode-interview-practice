# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive
    def goodNodes(self, root: TreeNode) -> int:
        self.numGoodNodes = 0
        
        def traverse(node, maxSoFar):
            if maxSoFar <= node.val:
                maxSoFar = node.val
                self.numGoodNodes += 1
            if node.right:
                traverse(node.right, maxSoFar)
            if node.left:
                traverse(node.left, maxSoFar)
        traverse(root, float("-inf"))
        return self.numGoodNodes
        
    
    # Iterative
    def goodNodes1(self, root: TreeNode) -> int:
        stack = [(root, float("-inf"))]
        numGoodNodes = 0
        while stack:
            node = stack.pop()
            if maxSoFar <= node.val:
                maxSoFar = node.val
                numGoodNodes += 1
            if node.right:
                stack.append(node.right, maxSoFar)
            if node.left:
                stack.append((node.left, maxSoFar))
        return numGoodNodes