class Solution:
    # BFS
    def minTime1(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
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
            hasApple[node] = True # Mark nodes on path

            for par in adj[node]:
                if par not in visited:
                    queue.append(par)
                    
        return sum(hasApple[1:]) * 2
    
    
    # DFS
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for s, t in edges:
            adj[t].append(s)
            adj[s].append(t)
        visited = set()
        
        
        def dfs(node):
            time = 0
            visited.add(node)
            for child in adj[node]:
                if child not in visited:
                    time += dfs(child)
            if (hasApple[node] or time):# and node != 0:
                        return time + 2
            return 0
        
        return max(dfs(0) - 2, 0) # Since we want to exclude the root node
    
    
    
    
    