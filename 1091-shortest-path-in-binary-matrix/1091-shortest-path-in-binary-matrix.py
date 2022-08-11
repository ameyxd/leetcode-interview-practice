class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        visited = set()
        queue = collections.deque()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        if grid[0][0] == 0:
            queue.append((1, (0, 0))) # Number of steps taken to visit this cell
        visited.add((0, 0))
        
        while queue:
            steps, cell = queue.popleft()
            r, c = cell[0], cell[1]
            if (r, c) == (M - 1, N - 1):
                return steps
            
            for i, j in dirs:
                nr, nc = r + i, c + j
                if nr in range(M) and nc in range(N) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    queue.append((steps + 1, (nr, nc)))
                    visited.add((nr, nc))
                    
        return -1