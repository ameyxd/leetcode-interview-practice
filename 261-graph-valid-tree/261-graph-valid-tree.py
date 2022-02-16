class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid tree will not have a cycle and will not have unconnected nodes
        
        if len(edges) != n - 1:
            return False
        
        indegree = {i: 0 for i in range(n)}
        adj = {i: [] for i in range(n)}
        
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            adj[n1].append(n2)
            adj[n2].append(n1)
            indegree[n1] += 1
            indegree[n2] += 1
        
        queue = collections.deque([k for k in indegree if indegree[k] == 1]) # Indegree will be 1 at the min since this the edges are undirected
        top_sort = []
        
        while queue:
            node = queue.popleft()
            top_sort.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    queue.append(nei)
        
        
        return all(val == 0 for val in indegree.values())