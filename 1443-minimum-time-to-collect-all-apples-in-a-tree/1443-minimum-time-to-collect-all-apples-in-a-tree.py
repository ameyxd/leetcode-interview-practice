class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Traverse in queue the nodes from apple to parent nodes, keep marking nodes that are in the path
        adj = defaultdict(list)
        for s, t in edges:
            if t in adj.keys(): adj[s].append(t)
            adj[t].append(s) # Store parent
        
        cost = 0
        queue = deque()
        visited = set()
        
        # Start queue with all nodes that have apples
        for i, app in enumerate(hasApple):
            if app:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            visited.add(node)
            hasApple[node] = True

            for par in adj[node]:
                if par not in visited:
                    queue.append(par)
                    
        return sum(hasApple[1:]) * 2