class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i: [] for i in range(n)}
        visited = set()
        
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        components = 0
        
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
                
        return components