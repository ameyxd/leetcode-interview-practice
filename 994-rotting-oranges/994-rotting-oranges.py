class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        queue, time = collections.deque(), 0
        minutes, fresh = 0, 0
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if not fresh: # the oranges are already all rotten
            return 0
        
        while queue:
            minutes += 1
            
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in steps:
                    newr, newc = r + dr, c + dc
                    if newr in range(rows) and newc in range(cols) and grid[newr][newc] == 1:
                        grid[newr][newc] = 2
                        fresh -= 1
                        queue.append((newr, newc))

        
        return minutes - 1 if not fresh else -1
        # Minutes - 1 because the last while loop will try to find neighbors of the last rotten orange, but since that doesn't affect any other oranges, we shouldn't include that round