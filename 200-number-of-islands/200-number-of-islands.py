class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in dirs:
                    new_row, new_col = row + dr, col + dc
                    if (new_row in range(rows) and new_col in range(cols) and grid[new_row][new_col] == "1" and (new_row, new_col) not in visited):
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
                
            
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
                    
        return islands