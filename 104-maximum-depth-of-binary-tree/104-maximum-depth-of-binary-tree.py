# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
#         # Recursive DFS Solution
#         left_height = 1 + self.maxDepth(root.left)
#         right_height = 1 + self. maxDepth(root.right)
#         return max(left_height, right_height)
    

#         # Iterative DFS Solution: Store (node, depth at that node) in stack, pop and check if res is greater than current depth and return res
#         stack = [(root, 1)]
#         res = 1
#         while stack:
#             node, depth = stack.pop()
#             if node: # Since I have set this code to include null nodes in stack
#                 res = max(res, depth)
#                 stack.append((node.left, depth + 1))
#                 stack.append((node.right, depth + 1))
#         return res
                
        # Iterative BFS Solution: Run for loop inside while queue exists, for the entire length of the queue, only update when out of for loop
        
        q, level = deque([root]), 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level