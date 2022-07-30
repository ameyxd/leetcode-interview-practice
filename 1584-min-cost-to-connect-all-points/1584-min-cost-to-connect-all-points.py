class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Minimum spanning tree
        n = len(points)
        adj = {i: [] for i in range(n)} # store list of cost, node
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Prims
        res = 0
        visited = set()
        minH = [(0, 0)] # cost, point
        
        while len(visited) < n:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minH, (neiCost, nei))
        
        return res
