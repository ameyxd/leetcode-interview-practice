class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] != 1: #reached out of bounds or water:
                return 1
            if (r, c) in visited:
                return 0

            visited.add((r, c))
                                    
            per = dfs(r - 1, c)
            per += dfs(r + 1, c)
            per += dfs(r, c - 1)
            per += dfs(r, c + 1)


            return per
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    return dfs(r, c)