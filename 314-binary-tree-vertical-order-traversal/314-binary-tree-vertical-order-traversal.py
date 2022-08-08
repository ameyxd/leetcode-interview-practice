# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        colTable = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, node_col_idx = queue.popleft()
            if node:
                colTable[node_col_idx].append(node.val)
                queue.append((node.left, node_col_idx - 1))
                queue.append((node.right, node_col_idx + 1))
                
        return [colTable[col] for col in sorted(colTable.keys())]