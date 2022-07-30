class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = {(0, 0)}
        heap = [(grid[0][0], (0, 0))]
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        
        while heap:
            a, (r, c) = heapq.heappop(heap)
            ans = max(a, ans)
            if r == c == n - 1:
                return ans
            for dr, dc in steps:
                newr, newc = r + dr, c + dc
                if newr in range(n) and newc in range(n) and (newr, newc) not in visited:
                    heapq.heappush(heap, (grid[newr][newc], (newr, newc)))
                    visited.add((newr, newc))
                    
        return ans