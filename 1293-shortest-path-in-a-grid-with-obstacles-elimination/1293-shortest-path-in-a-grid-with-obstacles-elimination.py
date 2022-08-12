class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = collections.deque([(0, 0, k, 0)])
        visited = set((0, 0, k))
        path = 0
        while queue:
            r, c, nk, path = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return path
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and (nr, nc, nk) not in visited:
                    if grid[nr][nc] == 1 and nk > 0:
                        visited.add((nr, nc, nk))
                        queue.append((nr, nc, nk - 1, path + 1))
                    elif grid[nr][nc] == 0:
                        visited.add((nr, nc, nk))
                        queue.append((nr, nc, nk, path + 1))
        print(path)
        return -1