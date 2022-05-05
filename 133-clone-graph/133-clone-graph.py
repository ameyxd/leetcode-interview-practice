"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
       # Recursive DFS with hashmap from old node to copy (new node)
        oldToNew = {}

        # DFS function returns the copy of the node it is passed
        def dfs(node):
            # if node is already cloned, get it from hashmap
            if node in oldToNew:
                return oldToNew[node]
            # else create clone and add to hashmap
            copy = Node(node.val)
            oldToNew[node] = copy
            
            # Run dfs recursively on each of the neighbors and add them to neighbors of copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor)) # remember that we are appending the (returned copy node of neighbor from dfs function) to the copied node
            return copy
        return dfs(node) if node else None