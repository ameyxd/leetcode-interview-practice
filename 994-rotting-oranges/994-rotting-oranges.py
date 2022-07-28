class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS - Level order traversal
        if not grid:
            return -1
        rows, cols = len(grid), len(grid[0])
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()
        minutes, fresh = 0, 0
        
        # populate the queue initially and count the number of fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if not fresh: # all oranges are already rotten
            return 0
        
        while queue:
            minutes += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in steps:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        # Rot the orange
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
                        
        return minutes - 1 if not fresh else -1
        # return minutes - 1 because the last while loop will try to find neighbors of the last rotten orange, but since that doesn't affect any other oranges, we shouldn't include that round
