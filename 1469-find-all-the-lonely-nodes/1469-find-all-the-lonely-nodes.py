# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([(root, False)]) # node, lonely
        res = []
        while queue:
            node, lonely = queue.popleft()
            if lonely:
                res.append(node.val)
            if node.right and node.left:
                lonely = False
            elif node.right or node.left:
                lonely = True
            
            if node.left:
                queue.append((node.left, lonely))
            if node.right:
                queue.append((node.right, lonely))
                
        return res
                