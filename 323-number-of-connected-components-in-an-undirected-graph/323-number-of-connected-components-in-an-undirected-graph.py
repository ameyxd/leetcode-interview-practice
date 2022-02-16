class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Run recursive DFS from any node, every time a new non-recursive call starts, that means that node was not reachable from any other node seen
        
        # initialize graph adjacency list
        adj = {i: [] for i in range(n)}
        
        # Set to keep track of which nodes are visited
        visited = set()

        # Build graph
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        # Recursive dfs while neighbor is not visited
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        components = 0
        
        # Run dfs on all nodes, every time a dfs call runs from this loop, it means that node was not reachable from other nodes, so that is the start of a new connected component
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
                
        return components