class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Djikstra's algorithm O(E log V)
        adj = {i + 1: [] for i in range(n)}
        
        for src, dest, time in times:
            adj[src].append((dest, time))

        minH = [(0, k)] # cost/time, node
        visited = set()
        time = 0
        
        while minH:
            w, n1 = heapq.heappop(minH)
            if n1 in visited:
                continue
            visited.add(n1)
            time = max(time, w)
            
            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minH, (w + w2, n2))
        return time if len(visited) == n else -1
        