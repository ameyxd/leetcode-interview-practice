# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # if node does not have a parent after deletion, add it to the res
        res = []
        deleteset = set(to_delete)
        queue = deque([(root, True)]) # Store node, noParent (i.e., will it be a new root)
        while queue:
            node, noParent = queue.popleft()
            if noParent and node.val not in deleteset:
                res.append(node)
            # If value is present in deleteset, that node will not have a parent
            noParent = node.val in deleteset
            
            if node.left:
                queue.append((node.left, noParent))
                if node.left.val in deleteset:
                    node.left = None
            if node.right:
                queue.append((node.right, noParent))
                if node.right.val in deleteset:
                    node.right = None
        return res