# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        res, queue = [], collections.deque([root])
        rev = False
        
        while queue:
            curr_level = []
            for i in range(len(queue)):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not rev:
                res.append(curr_level)
            else:
                res.append(curr_level[::-1]) # can also use deque to and appendleft each time reversal is needed
            rev = not rev
        return res