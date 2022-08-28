# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return None
        res = []
        queue = deque([(root, None, 0)]) # Store node, parent, depth
        while queue:
            for _ in range(len(queue)):
                node, parent, depth = queue.popleft()
                if node.val == x or node.val == y:
                    res.append((parent, depth))
                if node.left:
                    queue.append((node.left, node, depth + 1))
                if node.right:
                    queue.append((node.right, node, depth + 1))

        # res will have two nodes -> guaranteed in the constraints
        p1, d1 = res[0][0], res[0][1]
        p2, d2 = res[1][0], res[1][1]
        
        # Two parents aren't equal and two depths are the same
        return p1 != p2 and d1 == d2