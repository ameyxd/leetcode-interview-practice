class Solution:
    # Union Find - love this
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {v: -1 for v in range(1, len(edges) + 1)}
        def find(u):
            if parent[u] != -1:
                parent[u] = find(parent[u])
                return parent[u]
            else:
                return u # node is it's own parent
        
        # Returns true if adding an edge u, v creates a cycle
        def union(u, v):
            parent_u = find(u)
            parent_v = find(v)
            
            if parent_u == parent_v:
                # cycle is present
                return True
            else:
                # graph is still a tree without a cycle
                parent[parent_u] = parent_v
        redundant = None
        for u, v in edges:
            # Check if adding edge creates cycle 
            if union(u, v):
                redundant = [u, v] # we don't return u, v directly, because we need to return the last occurrence of a cycle creating edge
        
        return redundant
        
        
    # DFS solution        
    def findRedundantConnection_dfs(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(source, target): # essentially for cycle detection
            print(f"Visiting {source}")
            if source in visited:
                return False
            if source == target: # cycle exists
                return True
            visited.add(source)
            for nei in adj[source]:
                if dfs(nei, target):
                    return True
            return False      
        
        adj = {i + 1: [] for i in range(len(edges))} # Since we have one extra edge, the number of edges == number of vertices
        ans = []
        for n1, n2 in edges: # dfs every time you add an edge
            visited = set()
            if dfs(n1, n2):
                ans = [n1, n2] # since we want the last possible edge, return edge here
            adj[n1].append(n2)
            adj[n2].append(n1)
        return ans