# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         res, queue = [], deque([root])
        
#         while queue:
#             level_res = []
#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 level_res.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             res.append(level_res)
#         return res

        if not root:
            return []
        queue, res = [root], []
        while queue:
            level_res = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_res)
        return res