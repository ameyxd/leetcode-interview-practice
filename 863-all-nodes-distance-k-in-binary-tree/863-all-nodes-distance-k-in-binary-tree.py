# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Transform tree into graph and do bfs
        # build a parent dictionary from the tree, then traverse using parent dictionary
        if not root:
            return []
        adj = defaultdict(list)
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                adj[node.left.val].append(node.val)
                adj[node.val].append(node.left.val)
            if node.right:
                queue.append(node.right)
                adj[node.right.val].append(node.val)
                adj[node.val].append(node.right.val)
        
        res = []

        # Treat as graph and perform BFS
        visited = set()
        visited.add(target.val)
        q = deque([target.val])
        while q:
            if k == 0:
                return list(q)
            for _ in range(len(q)):
                node = q.popleft()
                for nei in adj[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            k -= 1
            
        return []